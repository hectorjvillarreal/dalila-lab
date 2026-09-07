#!/usr/bin/env bash
# Bundle de certificados TLS para el portal de la Secretaría.
#
# El portal presenta una hoja firmada por el intermedio Let's Encrypt YR1 y envía R10
# en el handshake. curl y Python fallan con «unable to get local issuer certificate».
# Los navegadores no lo notan porque descargan el intermedio faltante por AIA.
#
# NUNCA se resuelve con -k. Se resuelve con este bundle.
#
# TRAMPA: yr1.i.lencr.org sirve el certificado en DER. Un `cat` del DER produce un
# bundle que curl acepta sin protestar y que no arregla nada; el síntoma es idéntico
# al de no tener bundle. Hay que convertirlo.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p _certs && cd _certs

curl -sS --max-time 30 -o yr1.der http://yr1.i.lencr.org/
openssl x509 -inform DER -in yr1.der -outform PEM -out yr1.pem
curl -sS --max-time 30 -o root-yr-by-x1.pem https://letsencrypt.org/certs/gen-y/root-yr-by-x1.pem
cat /etc/ssl/certs/ca-certificates.crt yr1.pem root-yr-by-x1.pem > bundle.pem

echo "bundle.pem: $(wc -c < bundle.pem) bytes"
openssl x509 -in yr1.pem -noout -subject -issuer | sed 's/^/  /'
openssl x509 -in root-yr-by-x1.pem -noout -subject -issuer | sed 's/^/  /'
echo -n "  prueba contra el portal: "
curl -sS --cacert bundle.pem --max-time 25 -o /dev/null \
  -w "%{http_code}\n" https://www.pef.hacienda.gob.mx/

# `cotizantes.py`

Cotizantes por edad y sexo, prueba C y rotación.

Modelo de cohortes del Anexo H del Núcleo 13: envejece el stock de dic. 2025, aplica salidas, suma nuevos ingresantes con el vector por edad y calibra al total del libro (factor k). Prueba C: ocupados = CONAPO × tasa de ocupación ENIGH; formalidad implícita y edades con exceso; factor C2 como índice. Rotación: retención (edad+1, ant+1)/(edad, ant), advertencia R4.

- **Insumos:** I2, I3, I4
- **Salidas:** `cotizantes_edad_sexo`, `prueba_c_agregado`; tablas `prueba_c_*`, `rotacion_retencion_edad_sexo`
- **Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`

# figuras/

PDF de figuras generados por guion, incluidos con `\includegraphics`.

**Regla del proyecto:** si una figura resulta frágil dentro de LaTeX (`pgfplots` con muchos
puntos, o cualquier cosa que alargue la compilación), la salida es **generar su PDF por
separado** y traerlo con `\includegraphics`, conservando el guion y los datos que la
produjeron. Ningún minuto del reloj se va en depurar una figura.

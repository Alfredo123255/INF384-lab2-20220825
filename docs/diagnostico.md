1.1 
Defecto1: El job publicar no define needs: validar. Esto provoca que ambos trabajos se ejecuten en paralelo, permitiendo que se construya 
y se publique el artefacto aunque las pruebas unitarias o análisis de calidad fallen. Ya que publicar puede terminar antes de validar y
terminar antes

Defecto 2: El job publicar no restringe la rama de ejecución. El trigger on: push: no tiene filtro de rama, y el job publicar 
tampoco tiene una condición if: que lo limite. Esto provoca que cualquier push a cualquier rama (incluyendo ramas de feature sin terminar) construya y publique el artefacto, igual que un push a main. Se debería agregar if:
github.ref == 'refs/heads/main' al job publicar para que solo publique desde la rama principal.

Defecto3: Falta de verificación del Quality Gate de Sonar. El paso "Analisis de calidad" ejecuta el scanner y sube el análisis a SonarCloud, pero nunca espera ni comprueba si el Quality Gate pasó. Por diseño, SonarSource/sonarqube-scan
-action termina en éxito en cuanto el análisis se sube, sin importar si el código cumple los umbrales de calidad (bugs, cobertura, duplicación, etc.). Se debería agregar 
-Dsonar.qualitygate.wait=true a los args del scan (o un step posterior con SonarSource/sonarqube-quality-gate-action) para que el job realmente falle cuando el Quality Gate esté en rojo.

Defecto4:Se esta utilizando versiones de acción muy antiguas de Node 20 y github fuerza a Node.js 24

1.2
En este caso a pesar de que el pipeline parece eficiente con sus tiempos de 58s, 65s y 149s, no es verdad debido a que
ambos jobs se ejecutan en paralelo lo cual genera que puedan terminar antes, cuando esto deberia ser secuencial, ya que
primero deberia validar y despues publicar, por lo que el tiempo deberia ser mayor

1.3 Para mi grupo nos toco el caso de un value stream donde el cuello de botella era los procesos de QA debido a que tenian
un tiempo de espera muy alto para ejecutarse, pero para este caso el defecto 1 seria el mas relacionado, debido a que la 
restricción era que el flujo era secuencial, pero en este caso no debido a que los jobs son en paralelo por lo que no se podria
medir el lead time y encontrar el cuello de botella como fue en el caso de mi grupo con un QA de 1d y 8horas de leadtime

1.4 Sin entornos de despliegue automatizaods, unicamente se pueden medir y mover dos de las 4 metricas Dora
  1) Lead Time: Ya que se mide desde que el codigo se confirma hasta que esta validado y publicado en la rama main
  2) Tasa de fallo en los cambios: Mide la proporcion de ejecuciones que fallan debido a errores de codigo o calidad

En este caso se espera mover el lead time debido a que se piensa corregir el defecto 1 y poder tener el lead time verdadero
de la ejecución

1.5 La linea base era con un tiempo maximo de 149 segundos y un tiempo promedio de 90 segundos entre las 3 ejecuciones, 
la metra de la intervención es logar una ejecución secuencial del pipeline en 70 segundos

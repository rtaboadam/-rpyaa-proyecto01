# Statlog (Shuttle) Data Set 
### Reconocimiento de Patrones y Aprendizaje Automatizado

### Integrantes
* Lissarraga B. Iker
* Carreon T. Alfredo
* Taboada M. Ricardo


### Antes de comenzar
- Chequen *master* y de preferencia hagan pull o rebase por si se han actualizado archivos
- Instalar `virtualenv`
- Ejecutar `virtualenv env` dentro de la carpeta
- Agregar el `virtualenv` al `$PATH` es decir
	```sh 
	source env/bin/active
	```
- Instalar las dependencias del archivo `requirements.txt`
	```sh
	pip install -r requirements.txt
	```

### Estructura del código
```
.
├── main.py
├── README.md
├── reportes
│   └── README.md
├── requirements.txt
├── resources
│   ├── shuttle.doc
│   ├── shuttle.trn
│   └── shuttle.tst
└── slack.md

```

### Notas
- Me gustaría que proponieran como se va atacar el problema (como lo vamos a resolver)
  haciendo un .md en la carpeta de `reportes`
- Si ya tienen el reporte y algo de código, favor de subirlo a una nueva rama
  con su apellido, esto con el proposito de que los demas lo veamos
- Se propone el uso de `virualenv` con el proposito de poder trabajar en
en cualquier sistema operativo
- Si se agrego una nueva biblioteca favor de actualizar `requirements.txt`
	```sh
		pip freeze > requirements.txt
	```
	Esto último con el proposito de no tener conflictos con las bibliotecas

#### PS
Siento que esto es algo exagerado, disculpa


from peliculas import peliculas
from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/')
def buscar():
    return """
		<form action="/resultados" method="get">
			<input type="search" name="buscar" placeholder="Buscar">
			<select name="por">
                <option value="1">Titulo</option>
                <option value="2">Director</option>
            </select>
            <input type="submit" value="Buscar">
		</form>
	"""
@app.route('/resultados',methods=['GET'])
def resultados():
    busqueda = request.args.get('buscar')
    por = request.args.get("por")
    return render_template('resultados.html',peliculas=peliculas,busqueda=busqueda,por=por)

@app.route("/movie/<int:codigo>")
def movie_www(codigo):
    for x in peliculas:
        if x["codigo"]==codigo:
            peli=x
            break
    else:
        x=0
    return render_template("peli.html",pelicula=x)

#app.run("localhost",8080)
app.run(host="0.0.0.0", port=8080, debug=False)
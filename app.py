from flask import Flask, render_template, request
from cnx import conectar

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/flores")
def flores():
    return render_template("flores.html", flor=None, mensaje=None)

@app.route("/flores/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre_flor"]
    color = request.form["color"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    con = conectar()
    cur = con.cursor()
    consulta = "INSERT INTO flores (Nombre_flor, Color, Precio, Stock) VALUES (%s, %s, %s, %s)"
    cur.execute(consulta, [nombre, color, precio, stock])
    con.commit()
    cur.close()
    con.close()
    return render_template("flores.html", flor=None, mensaje="Flor guardada correctamente")

@app.route("/flores/modificar", methods=["POST"])
def modificar():
    id_flor = request.form["id"]
    nombre = request.form["nombre_flor"]
    color = request.form["color"]
    precio = request.form["precio"]
    stock = request.form["stock"]

    con = conectar()
    cur = con.cursor()
    consulta = """
        UPDATE flores
        SET Nombre_flor=%s, Color=%s, Precio=%s, Stock=%s
        WHERE Id=%s
    """
    cur.execute(consulta, [nombre, color, precio, stock, id_flor])
    con.commit()
    cur.close()
    con.close()
    return render_template("flores.html", flor=None, mensaje="Flor modificada correctamente")

@app.route("/flores/eliminar", methods=["POST"])
def eliminar():
    id_flor = request.form["id"]
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM flores WHERE Id=%s", [id_flor])
    con.commit()
    cur.close()
    con.close()
    return render_template("flores.html", flor=None, mensaje="Flor eliminada correctamente")

@app.route("/flores/buscar", methods=["POST"])
def buscar():
    id_flor = request.form["id"]
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM flores WHERE Id=%s", [id_flor])
    resultado = cur.fetchone()
    cur.close()
    con.close()

    if resultado:
        return render_template("flores.html", flor=resultado, mensaje=None)
    return render_template("flores.html", flor=None, mensaje="No se encontró la flor")

from flask import Flask, render_template, request, send_file
import mysql.connector

from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

@app.route("/flores/pdf")
def generar_pdf():

    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT Id, Nombre_Flor, Color, Precio, Stock
        FROM flores
    """)

    flores = cur.fetchall()

    cur.close()
    con.close()

    buffer = io.BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.setTitle("Reporte de Flores")

    # Título
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(200, 750, "REPORTE DE FLORES")

    # Encabezados
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(50, 710, "ID")
    pdf.drawString(90, 710, "Nombre")
    pdf.drawString(230, 710, "Color")
    pdf.drawString(330, 710, "Precio")
    pdf.drawString(410, 710, "Stock")

    # Datos
    y = 685

    pdf.setFont("Helvetica", 10)

    for flor in flores:

        pdf.drawString(50, y, str(flor[0]))
        pdf.drawString(90, y, str(flor[1]))
        pdf.drawString(230, y, str(flor[2]))
        pdf.drawString(330, y, str(flor[3]))
        pdf.drawString(410, y, str(flor[4]))

        y -= 25

        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 750

    pdf.save()

    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="application/pdf",
        download_name="reporte_flores.pdf",
        as_attachment=False
    )

if __name__ == "__main__":
    app.run(debug=True)
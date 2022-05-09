from fpdf import FPDF

class Estudiante:
    def __init__(self, nombre, semestre, profesor):
        self.nombre = nombre
        self.semestre = semestre
        self.profesor = profesor

file = open('alumnos.csv')
header = file.readline()
lista = []
for linea in file.readlines():
    separado = linea.strip().split(';')
    estudiante = Estudiante(separado[0], separado[1], separado[2])
    lista.append(estudiante)

lista.sort(key=lambda x: x.profesor)
profs = ['F. Ansaldi', 'G. Beltrán', 'A. Dourthe']


pdf = FPDF('P', 'mm', 'Letter')
pdf.set_font('Arial', '', 10)


for evaluador in profs:
    pdf.add_page()
    lastProf = lista[0].profesor
    for alumno in lista:
        if alumno.profesor != lastProf:
           pdf.add_page()
        pdf.cell(40, 9, alumno.nombre)
        pdf.cell(40, 9, 'Semestre: ' + alumno.semestre)
        pdf.cell(40, 9, 'Prof.: ' + alumno.profesor)
        pdf.cell(0, 9, 'Evaluador: ' + evaluador, 0, 1, 'R')
        pdf.cell(0, 9, '____________________________________________________________________________________________________', 0, 1)
        pdf.cell(0, 9, '____________________________________________________________________________________________________', 0, 1)
        pdf.cell(0, 9, '____________________________________________________________________________________________________', 0, 1)
        pdf.cell(0, 9, '____________________________________________________________________________________________________', 0, 1)
        pdf.cell(0, 9, '____________________________________________________________________________________________________', 0, 1)
        pdf.ln()
        lastProf = alumno.profesor


pdf.output('test.pdf', 'F')

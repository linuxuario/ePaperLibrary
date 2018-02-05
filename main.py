import epsimplelib

def hello_world():
	esp = epsimplelib.EPScreen('landscape') # eps = e-Ink Paper Screen
	esp.set_title("Hello world")

	esp.add_line((132, 70, 92, 135))
	esp.add_line((92, 135, 172, 135))
	esp.add_line((172, 135, 132, 70))

	esp.update_screen()

hello_world()

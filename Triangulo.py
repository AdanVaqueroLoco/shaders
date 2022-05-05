from Modelo import *

class Triangulo(Modelo):
    def __init__(self, shader, posicion_id, color_id, transformaciones_id):
        self.vertices = np.array(
            [
                -0.45,-0.1,0.0,1.0,  1.0,0.8,0.0,1.0,   #izquierda, abajo
                0.0,0.5,0.0,1.0,     0.0,1.0,0.0,1.0,   #Arriba
                0.5,-0.5,0.0,1.0,    0.0,0.0,1.0,1.0    #Derecha
            ], dtype="float32"
        )
        #Crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
        )
        super().__init_(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, direccion):
        cantidad_movimiento = glm.vec3(0,0,0)
        if direccion == self.
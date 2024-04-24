import subprocess

class AFD:
    def __init__(self, Q: set, sigma: set, delta: dict, q0: str, F: set):
        self.Q = Q         # estados
        self.sigma = sigma # alfabeto
        self.delta = delta # transiciones
        self.q0 = q0       # estado inicial
        self.F = F         # estados finales
    
    def evaluar_cadena(self, cadena: str) -> bool:
        estado_actual = self.q0
        for simbolo in cadena:
            estado_actual = self.delta.get((estado_actual, simbolo))
            
        print(f"{cadena}: {estado_actual in self.F}")
        return estado_actual in self.F

def write_dot_diagram_from_DFA(afd: AFD, filename="AFD", create_image=False) -> None:
    with open(f"{filename}.dot", "w") as f:
        print("/* transition diagram for DFA */", file=f)
        print("/* created by github.com/jesus-borja */", file=f)
        print("", file=f)
        print("digraph {", file=f)
        print("  rankdir = LR", file=f)
        print("", file=f)
        print("  \"Start\" [label = \"\", shape = none]", file=f)
        print("", file=f)

        # escribe todos los estados
        for q in afd.Q:
            if q in afd.F:
                print(f"  \"{q}\" [shape=doublecircle]", file=f)
            else:
                print(f"  \"{q}\" [shape=circle]", file=f)

        # escribe todas las aristas
        print(f"  \"Start\" -> \"{afd.q0}\"", file=f)
        for key, value in afd.delta.items():
            print(f"  \"{key[0]}\" -> \"{value}\" [label = \"{key[1]}\"]", file=f)
        
        print("  overlapse=false", file=f)
        print("}", file=f)

    if create_image: 
        create_png_diagram(filename, filename)
        
def create_png_diagram(dot_file: str, output_name: str):
    cmd = f"dot {dot_file}.dot -Tpng -o {output_name}.png"
    print(f"Creando imagen {output_name}.png con el archivo {dot_file}.dot")
    print(f"$ {cmd}")

    return_code = subprocess.run(cmd)
    if return_code.returncode == 0:
        print(f"Imagen \"{output_name}.png\" creada correctamente")
    else:
        print(f"No se pudo crear la imagen {output_name}.png")
        
if __name__ == "__main__":

    # ejemplo
    Q = {'q0', 'q1'}
    sigma = {'0', '1'}
    delta = {
       ('q0', '0'): 'q0',
       ('q0', '1'): 'q1',
       ('q1', '0'): 'q1',
       ('q1', '1'): 'q0',
    }
    q0 = 'q0'
    F = {'q0'}
    
    afd = AFD(Q, sigma, delta,q0, F)
    write_dot_diagram_from_DFA(afd, filename="ejemplo", create_image=True)
    
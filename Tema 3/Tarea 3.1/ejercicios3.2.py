import AFD

if __name__ == "__main__":

    # Para todos los ejercicios usamos el mismo alfabeto
    sigma = {'a', 'b'}

    # A) El lenguaje donde toda cadena tiene exactamente dos bs
    Q = {'q0', 'q1', 'q2', 'q3'}
    q0 = 'q0'
    F = {'q2'}
    delta = {
        ('q0', 'a'): 'q0',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',
    }
    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="A", create_image=True)
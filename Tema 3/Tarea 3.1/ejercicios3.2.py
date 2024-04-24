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

    # B) El lenguaje de las cadenas no vacias donde toda a está entre dos bs
    Q = {'q0', 'q1', 'q2',}
    q0 = 'q0'
    F = {'q1'}
    delta = {
        ('q0', 'a'): 'q2',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q1',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
    }
    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="B", create_image=True)

    # C) El lenguaje donde toda cadena contiene el sufijo aba
    Q = {'q0', 'q1', 'q2', 'q3',}
    q0 = 'q0'
    F = {'q3'}
    delta = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q0',
        ('q3', 'a'): 'q1',
        ('q3', 'b'): 'q2',
    }
    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="C", create_image=True)

    # D) El lenguaje donde ninguna cadena contiene las subcadenas aa ni bb
    Q = {'q0', 'q1', 'q2', 'q3',}
    q0 = 'q0'
    F = {'q0', 'q1', 'q2',}
    delta = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q2',
        ('q1', 'a'): 'q3',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q1',
        ('q2', 'b'): 'q3',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3',
    }
    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="D", create_image=True)

    # E) El lenguaje donde toda cadena contiene la subcadena baba
    Q = {'q0', 'q1', 'q2', 'q3', 'q4',}
    q0 = 'q0'
    F = {'q4',}
    delta = {
        ('q0', 'a'): 'q0',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q1',
        ('q2', 'a'): 'q0',
        ('q2', 'b'): 'q3',
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q1',
        ('q4', 'a'): 'q4',
        ('q4', 'b'): 'q4',
    }
    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="E", create_image=True)
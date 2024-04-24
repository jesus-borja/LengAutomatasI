import AFD

if __name__ == "__main__":

    ### Ejercicio 3.1 ###
    Q = {'q0', 'q1', 'q2', 'q3'}
    sigma = {'0', '1'}
    q0 = 'q0'
    delta = { ('q0', '0'): 'q2',
       ('q0', '1'): 'q1',
       ('q1', '0'): 'q1',
       ('q1', '1'): 'q2',
       ('q2', '0'): 'q1',
       ('q2', '1'): 'q3',
       ('q3', '0'): 'q3',
       ('q3', '1'): 'q1',
    }
    F = {'q0'}

    afd = AFD.AFD(Q, sigma, delta, q0, F)
    AFD.write_dot_diagram_from_DFA(afd, filename="ejercicio3.1", create_image=True)
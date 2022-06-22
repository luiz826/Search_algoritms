def acao(destino, custo):
    return {"destino": destino, 
            "custo": custo}   

estadosAspirador = [
    { 
        "estado": [0, 0, 0],
        "acoes": [acao([1, 0, 0], 1), acao([0, 1, 0], 1), acao([0, 0, 1], 1)]
    },
    { 
        "estado": [1, 0, 0],
        "acoes": [acao([1, 1, 0], 1), acao([1, 0, 1], 1)]
    },
    { 
        "estado": [0, 1, 0],
        "acoes": [acao([1, 1, 0], 1), acao([0, 1, 1], 1)]
    },
    { 
        "estado": [0, 0, 1],
        "acoes": [acao([1, 0, 1], 1), acao([0, 1, 1], 1)]
    },
    { 
        "estado": [1, 1, 0],
        "acoes": [acao([1, 1, 1], 1)]
    },
    { 
        "estado": [1, 0, 1],
        "acoes": [acao([1, 1, 1], 1)]
    },
    { 
        "estado": [0, 1, 1],
        "acoes": [acao([1, 1, 1], 1)]
    }
]

estadosAspirador2 = [
    { 
        "estado": [0, 0, 0, 0],
        "acoes": [acao([1, 0, 0, 0], 1), acao([0, 1, 0, 0], 1), 
                  acao([0, 0, 1, 0], 1), acao([0, 0, 0, 1], 1)]
    },
    { 
        "estado": [1, 0, 0, 0],
        "acoes": [acao([1, 1, 0, 0], 1), acao([1, 0, 1, 0], 1), acao([1, 0, 0, 1], 1)]
    },
    { 
        "estado": [0, 1, 0, 0],
        "acoes": [acao([1, 1, 0, 0], 1), acao([0, 1, 1, 0], 1), acao([0, 1, 0, 1], 1)]
    },
    { 
        "estado": [0, 0, 1, 0],
        "acoes": [acao([1, 0, 1, 0], 1), acao([0, 1, 1, 0], 1), acao([0, 0, 1, 1], 1)]
    },
    { 
        "estado": [0, 0, 0, 1],
        "acoes": [acao([1, 0, 0, 1], 1), acao([0, 1, 0, 1], 1), acao([0, 0, 1, 1], 1)]
    },
    { 
        "estado": [1, 1, 0, 0],
        "acoes": [acao([1, 1, 1, 0], 1), acao([1, 1, 0, 1], 1)]
    },
    { 
        "estado": [1, 0, 1, 0],
        "acoes": [acao([1, 1, 1, 0], 1), acao([1, 0, 1, 1], 1)]
    },
    { 
        "estado": [1, 0, 0, 1],
        "acoes": [acao([1, 1, 0, 1], 1), acao([1, 0, 1, 1], 1)]
    },
    { 
        "estado": [0, 1, 1, 0],
        "acoes": [acao([1, 1, 1, 0], 1), acao([0, 1, 1, 1], 1)]
    },
    { 
        "estado": [0, 1, 0, 1],
        "acoes": [acao([1, 1, 0, 1], 1), acao([0, 1, 1, 1], 1)]
    },
    { 
        "estado": [0, 0, 1, 1],
        "acoes": [acao([1, 0, 1, 1], 1), acao([0, 1, 1, 1], 1)]
    },
    {
        "estado": [0, 1, 1, 1],
        "acoes": [acao([1, 1, 1, 1], 1)]
    },
    {
        "estado": [1, 0, 1, 1],
        "acoes": [acao([1, 1, 1, 1], 1)]
    },
    {
        "estado": [1, 1, 0, 1],
        "acoes": [acao([1, 1, 1, 1], 1)]
    },
    {
        "estado": [1, 1, 1, 0],
        "acoes": [acao([1, 1, 1, 1], 1)]
    }
]


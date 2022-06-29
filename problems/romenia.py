from problems.utils import action

euclidean_heuristic_dict = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}

romania_states = [
    {
        "state": 'Arad',
        "actions": [ action('Zerind', 75, euclidean_heuristic_dict["Zerind"]),
                     action('Sibiu', 140, euclidean_heuristic_dict["Sibiu"]),
                     action('Timisoara', 118, euclidean_heuristic_dict["Timisoara"]) ]
    },

    {
        "state": 'Zerind',
        "actions": [ action('Arad', 75, euclidean_heuristic_dict["Arad"]),
                     action('Oradea', 71, euclidean_heuristic_dict["Oradea"]) ]
    },

    {
        "state": 'Timisoara',
        "actions": [ action('Arad', 117, euclidean_heuristic_dict["Arad"]), 
                     action('Lugoj', 111, euclidean_heuristic_dict["Lugoj"]) ]
    },

    {
        "state": 'Sibiu',
        "actions": [ action('Arad', 140, euclidean_heuristic_dict["Arad"]), 
                     action('Oradea', 151, euclidean_heuristic_dict["Oradea"]),
                     action('Fagaras', 99, euclidean_heuristic_dict["Fagaras"]),
                     action('Rimnicu Vilcea', 80, euclidean_heuristic_dict["Rimnicu Vilcea"])]
    },

    {
        "state": 'Oradea',
        "actions": [ action('Zerind', 71, euclidean_heuristic_dict["Zerind"]), 
                     action('Sibiu', 151, euclidean_heuristic_dict["Sibiu"]) ]
    },

    {
        "state": 'Lugoj',
        "actions": [ action('Timisoara', 111, euclidean_heuristic_dict["Timisoara"]),
                     action('Mehadia', 70, euclidean_heuristic_dict["Mehadia"]) ]
    },

    {
        "state": 'Mehadia',
        "actions": [ action('Lugoj', 70, euclidean_heuristic_dict["Lugoj"]),
                     action('Drobeta', 75, euclidean_heuristic_dict["Drobeta"]) ]
    },

    {
        "state": 'Drobeta',
        "actions": [ action('Mehadia', 75, euclidean_heuristic_dict["Mehadia"]), 
                     action('Craiova', 120, euclidean_heuristic_dict["Craiova"]) ]
    },

    {
        "state": 'Craiova',
        "actions": [ action('Drobeta', 120, euclidean_heuristic_dict["Drobeta"]), 
                     action('Rimnicu Vilcea', 146, euclidean_heuristic_dict["Rimnicu Vilcea"]), 
                     action('Pitesti', 138, euclidean_heuristic_dict["Pitesti"]) ]
    },

    {
        "state": 'Rimnicu Vilcea',
        "actions": [ action('Sibiu', 80, euclidean_heuristic_dict["Sibiu"]),
                     action('Craiova', 146, euclidean_heuristic_dict["Craiova"]), 
                     action('Pitesti', 97, euclidean_heuristic_dict["Pitesti"]) ]
    },

    {
        "state": 'Fagaras',
        "actions": [ action('Sibiu', 99, euclidean_heuristic_dict["Sibiu"]),
                     action('Bucharest', 211, euclidean_heuristic_dict["Bucharest"]) ]
    },

    {
        "state": 'Pitesti',
        "actions": [ action('Rimnicu Vilcea', 97, euclidean_heuristic_dict["Rimnicu Vilcea"]),
                     action('Craiova', 138, euclidean_heuristic_dict["Craiova"]), 
                     action('Bucharest', 101,euclidean_heuristic_dict["Bucharest"]) ]
    },

    {
        "state": 'Giurgiu',
        "actions": [ action('Bucharest', 90, euclidean_heuristic_dict["Bucharest"]) ]
    },

    {
        "state": 'Bucharest',
        "actions": [ action('Fagaras', 211, euclidean_heuristic_dict["Fagaras"]), 
                     action('Pitesti', 101, euclidean_heuristic_dict["Pitesti"]),
                     action('Giurgiu', 90, euclidean_heuristic_dict["Giurgiu"]),
                     action('Urziceni', 85, euclidean_heuristic_dict["Urziceni"]) ]
    },

    {
        "state": 'Urziceni',
        "actions": [ action('Bucharest', 85, euclidean_heuristic_dict["Bucharest"]), 
                     action('Vaslui', 142, euclidean_heuristic_dict["Vaslui"]),
                     action('Hirsova', 98, euclidean_heuristic_dict["Hirsova"]) ]
    },

    {
        "state": 'Hirsova',
        "actions": [ action('Urziceni', 98, euclidean_heuristic_dict["Urziceni"]),
                     action('Eforie', 86, euclidean_heuristic_dict["Eforie"]) ]
    },

    {
        "state": 'Eforie',
        "actions": [ action('Hirsova', 86, euclidean_heuristic_dict["Hirsova"]) ]
    },

    {
        "state": 'Vaslui',
        "actions": [ action('Urziceni', 142, euclidean_heuristic_dict["Urziceni"]), 
                     action('Iasi', 92, euclidean_heuristic_dict["Iasi"]) ]
    },

    {
        "state": 'Iasi',
        "actions": [ action('Vaslui', 92, euclidean_heuristic_dict["Vaslui"]), 
                     action('Neamt', 87, euclidean_heuristic_dict["Neamt"]) ]
    },

    {
        "state": 'Neamt',
        "actions": [ action('Iasi', 87, euclidean_heuristic_dict["Iasi"]) ]
    }
]

from problems.utils import action

romania_states = [
    {
        "state": 'Arad',
        "actions": [ action('Zerind', 75, 374), action('Sibiu', 140, 253), action('Timisoara', 118, 329) ]
    },

    {
        "state": 'Zerind',
        "actions": [ action('Arad', 75, 366), action('Oradea', 71, 380) ]
    },

    {
        "state": 'Timisoara',
        "actions": [ action('Arad', 117, 366), action('Lugoj', 111, 244) ]
    },

    {
        "state": 'Sibiu',
        "actions": [ action('Arad', 140, 366), action('Oradea', 151, 380), action('Fagaras', 99, 176),
                 action('Rimnicu Vilcea', 80, 193)]
    },

    {
        "state": 'Oradea',
        "actions": [ action('Zerind', 71, 374), action('Sibiu', 151, 253) ]
    },

    {
        "state": 'Lugoj',
        "actions": [ action('Timisoara', 111, 329), action('Mehadia', 70, 241) ]
    },

    {
        "state": 'Mehadia',
        "actions": [ action('Lugoj', 70, 244), action('Drobeta', 75, 242) ]
    },

    {
        "state": 'Drobeta',
        "actions": [ action('Mehadia', 75, 241), action('Craiova', 120, 160) ]
    },

    {
        "state": 'Craiova',
        "actions": [ action('Drobeta', 120, 242), action('Rimnicu Vilcea', 146, 193), action('Pitesti', 138, 100) ]
    },

    {
        "state": 'Rimnicu Vilcea',
        "actions": [ action('Sibiu', 80, 253), action('Craiova', 146, 160), action('Pitesti', 97, 100) ]
    },

    {
        "state": 'Fagaras',
        "actions": [ action('Sibiu', 99, 253), action('Bucharest', 211, 0) ]
    },

    {
        "state": 'Pitesti',
        "actions": [ action('Rimnicu Vilcea', 97, 193), action('Craiova', 138, 160), action('Bucharest', 101, 0) ]
    },

    {
        "state": 'Giurgiu',
        "actions": [ action('Bucharest', 90, 0) ]
    },

    {
        "state": 'Bucharest',
        "actions": [ action('Fagaras', 211, 176), action('Pitesti', 101, 100), action('Giurgiu', 90, 77),
                 action('Urziceni', 85, 80) ]
    },

    {
        "state": 'Urziceni',
        "actions": [ action('Bucharest', 85, 0), action('Vaslui', 142, 199), action('Hirsova', 98, 151) ]
    },

    {
        "state": 'Hirsova',
        "actions": [ action('Urziceni', 98, 80), action('Eforie', 86, 161) ]
    },

    {
        "state": 'Eforie',
        "actions": [ action('Hirsova', 86, 151) ]
    },

    {
        "state": 'Vaslui',
        "actions": [ action('Urziceni', 142, 80), action('Iasi', 92, 226) ]
    },

    {
        "state": 'Iasi',
        "actions": [ action('Vaslui', 92, 199), action('Neamt', 87, 234) ]
    },

    {
        "state": 'Neamt',
        "actions": [ action('Iasi', 87, 226) ]
    }
]


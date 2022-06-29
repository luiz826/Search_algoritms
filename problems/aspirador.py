from problems.utils import action

vacuum_states = [
    { 
        "state": [0, 0, 0],
        "actions": [action([1, 0, 0], 1, 1), action([0, 1, 0], 1, 1), action([0, 0, 1], 1, 1)]
    },
    { 
        "state": [1, 0, 0],
        "actions": [action([1, 1, 0], 1, 1), action([1, 0, 1], 1, 1)]
    },
    { 
        "state": [0, 1, 0],
        "actions": [action([1, 1, 0], 1, 1), action([0, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 0, 1],
        "actions": [action([1, 0, 1], 1, 1), action([0, 1, 1], 1, 1)]
    },
    { 
        "state": [1, 1, 0],
        "actions": [action([1, 1, 1], 1, 1)]
    },
    { 
        "state": [1, 0, 1],
        "actions": [action([1, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 1, 1],
        "actions": [action([1, 1, 1], 1, 1)]
    }
]

vacuum_states2 = [
    { 
        "state": [0, 0, 0, 0],
        "actions": [action([1, 0, 0, 0], 1, 1), action([0, 1, 0, 0], 1, 1), 
                  action([0, 0, 1, 0], 1, 1), action([0, 0, 0, 1], 1, 1)]
    },
    { 
        "state": [1, 0, 0, 0],
        "actions": [action([1, 1, 0, 0], 1, 1), action([1, 0, 1, 0], 1, 1), action([1, 0, 0, 1], 1, 1)]
    },
    { 
        "state": [0, 1, 0, 0],
        "actions": [action([1, 1, 0, 0], 1, 1), action([0, 1, 1, 0], 1, 1), action([0, 1, 0, 1], 1, 1)]
    },
    { 
        "state": [0, 0, 1, 0],
        "actions": [action([1, 0, 1, 0], 1, 1), action([0, 1, 1, 0], 1, 1), action([0, 0, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 0, 0, 1],
        "actions": [action([1, 0, 0, 1], 1, 1), action([0, 1, 0, 1], 1, 1), action([0, 0, 1, 1], 1, 1)]
    },
    { 
        "state": [1, 1, 0, 0],
        "actions": [action([1, 1, 1, 0], 1, 1), action([1, 1, 0, 1], 1, 1)]
    },
    { 
        "state": [1, 0, 1, 0],
        "actions": [action([1, 1, 1, 0], 1, 1), action([1, 0, 1, 1], 1, 1)]
    },
    { 
        "state": [1, 0, 0, 1],
        "actions": [action([1, 1, 0, 1], 1, 1), action([1, 0, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 1, 1, 0],
        "actions": [action([1, 1, 1, 0], 1, 1), action([0, 1, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 1, 0, 1],
        "actions": [action([1, 1, 0, 1], 1, 1), action([0, 1, 1, 1], 1, 1)]
    },
    { 
        "state": [0, 0, 1, 1],
        "actions": [action([1, 0, 1, 1], 1, 1), action([0, 1, 1, 1], 1, 1)]
    },
    {
        "state": [0, 1, 1, 1],
        "actions": [action([1, 1, 1, 1], 1, 1)]
    },
    {
        "state": [1, 0, 1, 1],
        "actions": [action([1, 1, 1, 1], 1, 1)]
    },
    {
        "state": [1, 1, 0, 1],
        "actions": [action([1, 1, 1, 1], 1, 1)]
    },
    {
        "state": [1, 1, 1, 0],
        "actions": [action([1, 1, 1, 1], 1, 1)]
    }
]

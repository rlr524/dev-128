x = ["a", "b", {
    "foo": 1,
    "bar": {
        "x": 10,
        "y": 20,
        "z": 30
    },
    "baz": 3
},
     "c",
     "d"
]

print(x[2]["bar"].get("z"))
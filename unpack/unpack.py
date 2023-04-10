def f(*args, **kwargs):
    print("positional: ", args)
    print("named: ", kwargs)
cat = 400
f(100, 200, 300, cat, bat=800, mat=500)
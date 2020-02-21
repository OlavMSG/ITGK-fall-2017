def vec():
    veca_input = input("x, y, z = ")
    x, y, z = veca_input.split(",")
    veca = [float(x), float(y), float(z)]
    return veca


def vec_print(vec, navn):
    vecnavn = "vec"+str(navn)
    print(vecnavn, "=", vec)


def skalarmulti(vec, skalar):
    ny_vec = [0, 0, 0]
    for i in range(3):
        ny_vec[i] = vec[i]*skalar
    return ny_vec

def lengde(vec):
    vec_l = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
    return vec_l


def prikkprodukt(vec1, vec2):
    ny_vec = [0, 0, 0]
    for i in range(3):
        ny_vec[i] = vec1[i]*vec2[i]
    prikkpro = sum(ny_vec)
    return prikkpro


vec1 = vec()
vec_print(vec1, 1)

vec2 = skalarmulti(vec1, 2)
vec_print(vec2, 2)

vec1_l = lengde(vec1)
print("vec1 har lengde", vec1_l)
vec2_l = lengde(vec2)
print("vec2 har lengde", vec2_l)
print("Forholdet vec1/vec2 er", vec1_l/vec2_l)

prikkpro12 = prikkprodukt(vec1, vec2)
print("vec1*vec2 =", prikkpro12)

vec3 = vec()
vec_print(vec3, 3)
prikkpro13 = prikkprodukt(vec1, vec3)
print("vec1*vec3 =", prikkpro13)




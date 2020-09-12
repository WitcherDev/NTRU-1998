from random import randint

def Central_Lift(old_list, q):
    new_list = []
    for a in old_list:
        a = int(a)
        if q/2 < a:
            new_list.append(a-q)
        elif a < -1* q/2:
            new_list.append(a + q)
        else:
            new_list.append(a)
    return new_list

def Central_Lift2(old_list, q):
    new_list = []
    for a in old_list:
        a = int(a)
        if a == 2:
            new_list.append(-1)
        elif a == 0:
            new_list.append(0)
        elif a == 1:
            new_list.append(1)
    return new_list

def rand_tab_message(N, p):
    m_tab = []
    for i in range(N):
        m_tab.append(randint(int(-1/2 *p), int(1/2 *p)))
    return m_tab


def inverse_fp_and_fq(N, p, q, d1, d2):
    flag_func = 1
    while(flag_func):
        flag_func = 0
        poly_tab_f = rand_poly_tab(N, d1, d2)
        fq = Rq(poly_tab_f)
        fp = Rp(poly_tab_f)
        try:
            fqprim = fq**(-1)
        except ZeroDivisionError as e:
            flag_func = 1
        try:
            fpprim = fp**(-1)
        except ZeroDivisionError as e:
            flag_func = 1
    f = Rz(poly_tab_f)
    return f, fpprim, fqprim

def rand_poly_tab(N, d1, d2):
    poly_list_1 = []
    for i in range(0, d1):
        num = randint(0, N - 1)
        flag = 1
        while(flag):
            if num not in poly_list_1:
                flag = 0
            else:
                num = randint(0, N - 1)
        poly_list_1.append(num)
    poly_list_2 = []
    for i in range(d2):
        num = randint(0, N - 1)
        flag = 1
        while(flag):
            if num not in poly_list_1 and num not in poly_list_2:
                flag = 0
            else:
                num = randint(0, N - 1)
        poly_list_2.append(num)
    poly_tab = []
    for i in range(N):
        if i in poly_list_1:
            poly_tab.append(1)
        elif i in poly_list_2:
            poly_tab.append(-1)
        else:
            poly_tab.append(0)
    return poly_tab

def generate_N(p):
    while(True):
        N = randint(100, 512)
        if gcd(N, p) == 1:
            return N

def generate_q(N, p):
    while(True):
        q = random_prime(512, False, 4)
        if (N)/2 < q < N - 1 and q != p:
            return q

success_rate = 0

for j in range(1,11):

    df = randint(4, 12)
    dg = randint(4, 12)
    dr = randint(4, 12)
    p = random_prime(200, False, 3)
    N = generate_N(p)
    q = generate_q(N, p)

    print("N {}; p {}; q {}; d {};" .format(N, p, q, df))
    for i in range(1,1001):
        Fp = GF(p)
        Fq = GF(q)

        FZ.<a> = PolynomialRing(ZZ)
        Rz.<x> = FZ.quotient((a**N)-1)

        FQ.<b> = PolynomialRing(GF(q))
        Rq.<y> = FQ.quotient((b**N)-1)

        FP.<c> = PolynomialRing(GF(p))
        Rp.<z> = FP.quotient((c**N)-1)

        f, fp, fq = inverse_fp_and_fq(N, p, q, df + 1, df)

        g = Rz(rand_poly_tab(N, dg, dg))
        r = Rz(rand_poly_tab(N, dr, dr))

        m = Rz(rand_tab_message(N, p))

        h = p * fq * Rq(list(g))

        e = Rq(list(r)) * h + Rq(list(m))

        a = e * Rq(list(f))
        a = Rz(Central_Lift(list(a), q))
        dm = Rp(list(a)) * fp
        dm = Rz(Central_Lift(list(m), p))

        if dm == m:
            success_rate += 1

        else:
            print("Decryption failed")
print success_rate

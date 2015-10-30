import prompt, math
from goody import irange
from rational import Rational

def compute_e(n):
    answer = Rational(1)
    for i in irange(1,n):
        answer += Rational(1,math.factorial(i))
    return answer
print (Rational(1,123).approximate(10))
print (Rational(314159,100000).best_approximation(2))

# Driver: prompts and executes commands (can all compute_e)
while True:
    try:
        exec(prompt.for_string('Command'))
    except Exception as report:
        import traceback
        traceback.print_exc()
     
    
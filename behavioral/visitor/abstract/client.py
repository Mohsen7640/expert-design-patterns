from behavioral.visitor.abstract.visitors.algorithm import Algorithm
from behavioral.visitor.abstract.elements.elementA import ElementA

if __name__ == '__main__':
    algorithm = Algorithm()
    element_a = ElementA()

    element_a.accept(visitor=algorithm)

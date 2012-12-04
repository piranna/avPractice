'''
Created on 04/12/2012

@author: piranna

Perceptron class based on original work of Evan Fosmark
http://www.evanfosmark.com/2011/07/a-simple-perceptron-implementation-in-python
'''


class Perceptron(object):
    def __init__(self, weights=None, threshold=0.5):
        "Constructor"
        self.threshold = threshold
        self.weights = weights
        self.verbose = False

    def output(self, input_vector):
        "Check a input vector against the current threshold"

        return self._total(input_vector) >= self.threshold

    def train(self, training_set, alpha=0.1, end_after=100):
        """Train the perceptron

        @param training_set: data used to train the perceptron
        @type training_set: dict
        @param alpha: factor of training
        @type alpha: float
        @param end_after: maximus number of iterations before stop. If set to
            None, it doesn't stop
        @type end_after: integer or None

        @return: the number of needed iterations
        @rtype: integer
        """

        # weights was not defined, set an empty list
        if not self.weights:
            self.weights = [0] * len(training_set.keys()[0])

        result = 0
        updated = True

        while(updated):
            updated = False

            for input_vector, test in training_set.items():
                output = self.output(input_vector)

                if output != test:
                    self._update_weights(alpha, test, output, input_vector)
                    self._update_threshold(alpha, test, output)

                    updated = True

            result += 1

            # Check if we achieved the limit of iterations (if any)
            if end_after and result >= end_after:
                break

        return result

    def test(self, training_set):
        "Check if the perceptron is correctly trained for a test suite"

        for input_vector, test in training_set.items():
            if self.output(input_vector) != test:
                return False

        return True

    def _total(self, input_vector):
        "Return the output value of the perceptron for an input"

        total = 0

        for weight, input_value in zip(self.weights, input_vector):
            total += weight * input_value

        return total

    def _update_weights(self, alpha, test, output, input_vector):
        "Update the weights of the of the diferent variables of the perceptron"

        for i in range(len(self.weights)):
            self.weights[i] += alpha * (test - output) * input_vector[i]

    def _update_threshold(self, alpha, test, output):
        "Update the threshold of the perceptron"

        self.threshold -= alpha * (test - output)


if __name__ == '__main__':
    nand_set = {(0, 0): 1,
                (0, 1): 1,
                (1, 0): 1,
                (1, 1): 0}

    nn = Perceptron()
    iterations = nn.train(nand_set, alpha=.2)  # alpha is the learning rate
    print "Trained in {0} iterations.".format(iterations)
    print "Correct?", nn.test(nand_set)
    print "Weights: {0}, Threshold: {1}".format(nn.weights, nn.threshold)

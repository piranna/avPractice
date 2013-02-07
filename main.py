'''
Created on 07/02/2013

@author: piranna
'''

if __name__ == '__main__':
    import argparse
    import json

    from perceptron import Perceptron

    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--weights', default='null',
                        type=argparse.FileType('r'),
                        help='file containing the weights in JSON format')

    parser.add_argument('--train_dir', help='dir with images for training')
    parser.add_argument('--alpha', help='learning rate with this training dir')

    parser.add_argument('test_dir', help='dir with images for testing')

    args = parser.parse_args()

    print args

    # Load weights
    weights = json.loads(args.weights.read())

    # Load train dir & alpha
    try:
        train_dir = args.train_dir
    except Exception as e:
        print(e)
    else:
        alpha = args.alpha

    # Load test dir
    test_dir = args.test_dir

    # Run perceptron
    perceptron = Perceptron(weights)

    # Return results
    for city in path:
        print(city)

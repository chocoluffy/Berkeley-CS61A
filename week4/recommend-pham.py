"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map
from data import RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact

def find_closest(location, centroids):
    """Return the item in CENTROIDS that is closest to LOCATION. If two
    centroids are equally close, return the first one.

    >>> find_closest([3, 4], [[0, 0], [2, 3], [4, 3], [5, 5]])
    [2, 3]
    """
    "*** YOUR CODE HERE ***"
    distances=[]
    for pair in centroids:
        distances.append(distance(location, pair))
    for pair in centroids:
        if min(distances)==distance(location, pair):
            return pair

def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [4], [2, 1]]
    """
    # Optional: This implementation is slow because it traverses the list of
    #           pairs one time for each key. Can you improve it?
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]

def group_by_centroid(restaurants, centroids):
    """Return a list of lists, where each list contains all restaurants nearest
    to some item in CENTROIDS. Each item in RESTAURANTS should appear once in
    the result, along with the other restaurants nearest to the same centroid.
    No empty lists should appear in the result.
    """
    "*** YOUR CODE HERE ***"
    return group_by_first([[find_closest(restaurant_location(r), centroids), r] for r in restaurants])

def find_centroid(restaurants):
    """Return the centroid of the locations of RESTAURANTS."""
    "*** YOUR CODE HERE ***"
    centroid_latitude=mean([restaurant_location(r)[0] for r in restaurants])
    centroid_longitude=mean([restaurant_location(r)[1] for r in restaurants])
    return [centroid_latitude, centroid_longitude]

def k_means(restaurants, k, max_updates=100):
    """Use k-means to group RESTAURANTS by location into K clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing K different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        "*** YOUR CODE HERE ***"
        grouped= group_by_centroid(restaurants, old_centroids)
        centroids=[find_centroid(r) for r in grouped]
        n += 1
    return centroids

def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for USER by performing least-squares linear regression using FEATURE_FN
    on the items in RESTAURANTS. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}

    xs = [feature_fn(r) for r in restaurants]
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants]

    "*** YOUR CODE HERE ***"
    data_points=zip(xs, ys)
    S_xx, S_yy, S_xy = 0, 0, 0
    for x in xs:
        S_xx += pow((x - mean(xs)), 2)
    for y in ys:
        S_yy += pow((y - mean(ys)), 2)
    for x, y in data_points:
        S_xy += (x - mean(xs))*(y - mean(ys))

    b = S_xy/S_xx
    a, r_squared =  mean(ys)-b*mean(xs), pow(S_xy, 2)/(S_xx*S_yy)  # REPLACE THIS LINE WITH YOUR SOLUTION

    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared

def best_predictor(user, restaurants, feature_fns):
    """Find the feature within FEATURE_FNS that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A dictionary from restaurant names to restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = list(user_reviewed_restaurants(user, restaurants).values())
    "*** YOUR CODE HERE ***"
    predicter_list, r_squared_list=[], []
    for fn in feature_fns:
        x, y = find_predictor(user, reviewed, fn)
        predicter_list.append(x)
        r_squared_list.append(y)
    zipped=zip(predicter_list, r_squared_list)
    return max(zipped, key=lambda x: x[1])[0]

    """r_squared_list = []
    index=0
    while index <= len(feature_fns)-1:
        r_squared_list.append([find_predictor(user, reviewed, feature_fns[index])])
        index+=1

    return max(r_squared_list, key=lambda x: x[-1])[0]"""

def rate_all(user, restaurants, feature_functions):
    """Return the predicted ratings of RESTAURANTS by USER using the best
    predictor based a function from FEATURE_FUNCTIONS.

    Arguments:
    user -- A user
    restaurants -- A dictionary from restaurant names to restaurants
    """
    # Use the best predictor for the user, learned from *all* restaurants
    # (Note: the name RESTAURANTS is bound to a dictionary of all restaurants)
    predictor = best_predictor(user, RESTAURANTS, feature_functions)
    "*** YOUR CODE HERE ***"
    user_reviewed= user_reviewed_restaurants(user, restaurants)
    user_reviewed={name: user_rating(user, name) for name in user_reviewed}
    user = user_reviewed.keys()
    user_reviewed.update({r: predictor(restaurants[r]) for r in restaurants if r not in user})
    return user_reviewed

def search(query, restaurants):
    """Return each restaurant in RESTAURANTS that has QUERY as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """
    "*** YOUR CODE HERE ***"
    return [restaurant for restaurant in restaurants if query in restaurant_categories(restaurant)]

def feature_set():
    """Return a sequence of feature functions."""
    return [restaurant_mean_rating,
            restaurant_price,
            restaurant_num_ratings,
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]

@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    args = parser.parse_args()

    # Select restaurants using a category query
    if args.query:
        results = search(args.query, RESTAURANTS.values())
        restaurants = {restaurant_name(r): r for r in results}
    else:
        restaurants = RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        ratings = {name: user_rating(user, name) for name in restaurants}

    # Draw the visualization
    restaurant_list = list(restaurants.values())
    if args.k:
        centroids = k_means(restaurant_list, min(args.k, len(restaurant_list)))
    else:
        centroids = [restaurant_location(r) for r in restaurant_list]
    draw_map(centroids, restaurant_list, ratings)

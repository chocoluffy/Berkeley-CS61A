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
    min_dis=min(distance(location, i) for i in centroids)
    for i in range(len(centroids)):
        if distance(location, centroids[i])==min_dis:
            return centroids[i]


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
    for key, _ in pairs:  #the inner list should have same length
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
    location_list=[restaurant_location(i) for i in restaurants]
    location_cloest_central=[find_closest(j,centroids) for j in location_list]
    pair=[[location_cloest_central[k],restaurants[k]] for k in range(len(location_list)) ]
    return group_by_first(pair)

def find_centroid(restaurants):
    """Return the centroid of the locations of RESTAURANTS."""
    "*** YOUR CODE HERE ***"
    location_list=[restaurant_location(i) for i in restaurants]
    latitude=mean([i[0] for i in location_list])
    longitude=mean([i[1] for i in location_list])
    return [latitude,longitude]

def k_means(restaurants, k, max_updates=100):
    """Use k-means to group RESTAURANTS by location into K clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing K different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        "*** YOUR CODE HERE ***"
        lst_same_cent=group_by_centroid(restaurants,centroids)
        centroids=[find_centroid(i) for i in lst_same_cent]
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
    sxx_sub=[i-mean(xs) for i in xs]
    sxx=0
    for i in range(len(sxx_sub)):
        sxx+=sxx_sub[i]*sxx_sub[i]

    syy_sub=[j-mean(ys) for j in ys]
    syy=0
    for j in range(len(syy_sub)):
        syy+=syy_sub[j]*syy_sub[j]
    sxy=0
    for k in range(len(sxx_sub)):
        sxy+=sxx_sub[k]*syy_sub[k]

    b=sxy/sxx
    a=mean(ys)-b*mean(xs)
    r_squared=sxy*sxy/(sxx*syy)

     # REPLACE THIS LINE WITH YOUR SOLUTION

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
    predictor_lst=[]
    r_squared_lst=[]
    for i in feature_fns:
        predictor_tmp, r_squared_tmp=find_predictor(user,reviewed,i)
        predictor_lst+=[predictor_tmp]
        r_squared_lst+=[r_squared_tmp]
    max_score=max(r_squared_lst)
    for j in range(len(r_squared_lst)):
        if r_squared_lst[j]==max_score:
            return predictor_lst[j]


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
    reviewed=list(user_reviewed_restaurants(user, restaurants).keys())
    new_dict= dict(restaurants)
    for i in list(restaurants.keys()):
        if i in reviewed:
            new_dict[i]=user_rating(user,i)
        else:
            new_dict[i]=predictor(restaurants[i])
    return new_dict


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

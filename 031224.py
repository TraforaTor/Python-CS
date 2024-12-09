from icecream import ic

GLOBAL_CONSTANT = "I'm a liar, I'm not a constant"

def main():
    friends = {'Giovanni': 'squillero@polito.it', 'Mick': 'jagger@rollingstones.com'}
    friends[(23,10)] = 'Giovanni'
    friends[42] = ['Meaning', 'of', 'life']
    print(friends['Giovanni'])
    friends[42].extend(['Universe', 'Everything Else'])
    ic(friends)
    ic(friends.keys())
    ic(friends.values())
    ic(friends.items())

    for f in friends:
        print(f"{f} -> {friends[f]}")

    for v in friends.values():
        print(f"? -> {v}")
    
    for f, v in friends.items():
        print(f"{f} -> {v}")
if __name__ == '__main__':
    main()
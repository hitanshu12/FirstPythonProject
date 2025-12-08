import time


def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {start_time} - {end_time} seconds")
        return result
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} Tea...")
    time.sleep(steep_time)
    print("Your Tea is done...")

@timer_dec
def make_matcha():
    print(f"Brewing Matcha...")
    time.sleep(1)
    print("Your Matcha is done...")


brew_tea("green", 1)
brew_tea(tea_type='Black', steep_time=2)
make_matcha()

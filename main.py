from pprint import pprint

from robots.wikipedia_robot import PersonWikipediaRobot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = PersonWikipediaRobot()


def main():
    robot.say_hello()
    for scientist in SCIENTISTS:
        person_data = robot.find_person(scientist)
        pprint(person_data)
    robot.say_goodbye()


if __name__ == "__main__":
    main()

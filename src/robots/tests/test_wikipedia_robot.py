from datetime import datetime

import pytest

from config import SCIENTISTS
from dto.person_profile import PersonProfile
from robots.wikipedia_robot import PersonWikipediaRobot


@pytest.fixture
def person_wikipedia_robot() -> PersonWikipediaRobot:
    return PersonWikipediaRobot()


@pytest.fixture
def person_profile_albert_einstain() -> PersonProfile:
    return PersonProfile(
        name="Albert Einstein",
        birth_date=datetime(1879, 3, 14).date(),
        death_date=datetime(1955, 4, 18).date(),
        description="""Albert Einstein (/ˈaɪnstaɪn/ EYEN-styne;[4] German: [ˈalbɛʁt ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18 April 1955) was a German-born theoretical physicist,[5] widely acknowledged to be one of the greatest and most influential physicists of all time. Best known for developing the theory of relativity, he also made important contributions to the development of the theory of quantum mechanics. Relativity and quantum mechanics are the two pillars of modern physics.[1][6] His mass–energy equivalence formula E = mc2, which arises from relativity theory, has been dubbed "the world's most famous equation".[7] His work is also known for its influence on the philosophy of science.[8][9] He received the 1921 Nobel Prize in Physics "for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect",[10] a pivotal step in the development of quantum theory. His intellectual achievements and originality resulted in "Einstein" becoming synonymous with "genius".[11] Einsteinium, one of the synthetic elements in the periodic table, was named in his honor.[12]""" # noqa: E501
    )


def test_wikipedia_robot_find_article(person_wikipedia_robot: PersonWikipediaRobot):
    for person_name in SCIENTISTS:
        slug_person_name = person_name.replace(" ", "_")
        person_wikipedia_robot.find_article(person_name)
        person_wikipedia_robot.browser.location_should_contain(slug_person_name)


def test_wikipedia_robot_find_person(
    person_wikipedia_robot: PersonWikipediaRobot,
    person_profile_albert_einstain: PersonProfile,
):
    expected_person = person_wikipedia_robot.find_person(person_profile_albert_einstain.name)
    assert expected_person == person_profile_albert_einstain
    assert expected_person.age == person_profile_albert_einstain.age
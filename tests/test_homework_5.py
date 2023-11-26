from selene import browser, have, be
import time
import random
browser.config.timeout = 50
browser.config.base_url = "https://app.qa.guru/automation-practice-form/"

Name = ("Anna", "Maya", "Olga", "Criss",
        "Nina", "Masha", "Katya")
Surname = ("Bulgakova", "Dobraya", "Popova")
Address = ("44 Thomas Ridges North Dalestad PO35 5XS","51 Adam Loop Laurenfurt RG19 8JZ","298 Hunt Green Harryfurt LE3 0BF")

def test_fill_form():
    browser.open('/')
    browser.element('[class="MuiBox-root css-1vpe9z"]').should(be.visible).click()
    browser.element('[id=":r0:"]').should(be.blank).type(random.choice(Name))
    browser.element('[id=":r1:"]').should(be.blank).type(random.choice(Surname))
    browser.element('[id=":r2:"]').should(be.blank).type('Magomedova@gmail.com')
    browser.element('[id=":r3:"]').type('9909999999')
    browser.element('[data-testid=language]').element('..').click()
    browser.all('#menu- [role=option]').by(have.exact_text('English')).first.click()
    time.sleep(3)
    browser.element('[role="radiogroup"] [value="Male"]').click()
    browser.element('[type="checkbox"][value="Sports"]').click()
    time.sleep(10)
    browser.element('[data-testid="subjects"]').element('..').click()
    browser.all('#menu- [role=option]').element_by(have.attribute('data-value').value('Accounting')).click().press_escape()
    browser.element('[data-testid="stateCity"]').element('..').click()
    time.sleep(3)
    browser.all('#menu- [role=option]').element_by(have.attribute('data-value').value('Illinois')).click().press_escape()
    browser.element('[data-testid="address"]').type((random.choice(Address)))
    time.sleep(3)
    browser.element('[type="submit"]').click()
    assert browser.element('[class="MuiTypography-root MuiTypography-h4 css-rq8zac"]').should(be.visible)







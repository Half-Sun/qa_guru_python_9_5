from selene import browser, have, be
import time

browser.config.timeout = 40
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.base_url = "http://app.qa.guru/automation-practice-form/"


def test_fill_form():
    browser.open('/')
    browser.element('[class="MuiBox-root css-1vpe9z"]').should(be.visible).click()
    browser.element('[id=":r0:"]').should(be.blank).type("Olga")
    browser.element('[id=":r1:"]').should(be.blank).type("Someone")
    browser.element('[id=":r2:"]').should(be.blank).type('Pochta@gmail.com')
    browser.element('[id=":r3:"]').type('9909999999')
    browser.element('[data-testid="address"]').type("This is address").press_escape()
    browser.element('[data-testid="CalendarIcon"]').click()
    browser.all('[role="gridcell"]').element_by(
    have.attribute('data-timestamp').value('1698872400000')).click().press_escape()
    time.sleep(3)
    browser.element('[data-testid=language]').element('..').click()
    browser.all('#menu- [role=option]').by(have.exact_text('English')).first.click()
    time.sleep(3)
    browser.element('[role="radiogroup"] [value="Male"]').click()
    browser.element('[type="checkbox"][value="Sports"]').click()
    time.sleep(10)
    browser.element('[data-testid="subjects"]').element('..').click()
    browser.all('#menu- [role=option]').element_by(
    have.attribute('data-value').value('Accounting')).click().press_escape()
    browser.element('[data-testid="stateCity"]').element('..').click()
    browser.all('#menu- [role=option]').element_by(
    have.attribute('data-value').value('Illinois')).click().press_escape()
    browser.element('[type="submit"]').click()
    browser.element('[class="MuiTypography-root MuiTypography-h4 css-rq8zac"]').should(have.exact_text('Thank you for submitting the form'))
    browser.element('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]').should(have.exact_text('Olga'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[1].should(have.text('Someone'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[2].should(have.text('Pochta@gmail.com'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[3].should(have.text('Male'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[4].should(have.text('+1 990 999 9999'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[5].should(have.text('02/11/2023'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[6].should(have.text('Accounting'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[7].should(have.text('Sports'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[8].should(have.text('English'))
    browser.all('[class="MuiTypography-root MuiTypography-body1 css-1qye57c"]')[9].should(have.text('This is address'))






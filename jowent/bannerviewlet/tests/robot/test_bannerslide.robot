# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s another.product -t test_bannerslide.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src another.product.testing.ANOTHER_PRODUCT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_bannerslide.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a BannerSlide
  Given a logged-in site administrator
    and an add bannerslide form
   When I type 'My BannerSlide' into the title field
    and I submit the form
   Then a bannerslide with the title 'My BannerSlide' has been created

Scenario: As a site administrator I can view a BannerSlide
  Given a logged-in site administrator
    and a bannerslide 'My BannerSlide'
   When I go to the bannerslide view
   Then I can see the bannerslide title 'My BannerSlide'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add bannerslide form
  Go To  ${PLONE_URL}/++add++jowent.bannerviewlet.bannerslide

a bannerslide 'My BannerSlide'
  Create content  type=jowent.bannerviewlet.bannerslide  id=my-bannerslide  title=My BannerSlide


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the bannerslide view
  Go To  ${PLONE_URL}/my-bannerslide
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a bannerslide with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the bannerslide title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

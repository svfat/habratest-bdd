from behave import given, when, then

@then(u'I should see link contents url "{content}"')
def i_should_see_link_contents_url(context, content):
    msg = context.browser.find_link_by_partial_href(content).first
    assert msg

@when(r'I visit url "{url}"')
def i_visit_url(context, url):
    br = context.browser
    br.visit(url)

@given(u'I am a visitor')
def i_am_a_visitor(context):
    pass

@then(u'I should see "{text}" somewhere in page')
def i_should_see_text_somwhere_in_page(context, text):
    assert text in context.browser.html

@when(u'I click link contents "{text}"')
def i_click_link_contents_text(context, text):
    link = context.browser.find_link_by_text(text).first
    assert link
    link.click()

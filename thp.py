from telegraph import Telegraph

telegraph = Telegraph()

telegraph.create_account(short_name='1337')

response = telegraph.create_page(
    'Hey',
    html_content='<p>Hello, !</p> <iframe allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowfullscreen="allowfullscreen" scrolling="no" src="https://www.facebook.com/plugins/video.php?height=314&amp;href=https%3A%2F%2Fwww.facebook.com%2Fkunuznews%2Fvideos%2F174479601495722%2F&amp;show_text=false&amp;width=560&amp;t=0" style="border:none;overflow:hidden" width="560" height="314" frameborder="0"></iframe>'
)

print('https://telegra.ph/{}'.format(response['path']))
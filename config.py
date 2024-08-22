# https://github.com/serv0id/skipera
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-coursera-application': 'ondemand',
    'x-coursera-version': 'cde5f24972aff1ebd6447e911113e781b9c52f7f',
    'x-requested-with': 'XMLHttpRequest',
}
BASE_URL = 'https://www.coursera.org/api/'
EMAIL = 'ayushshukla23@lpu.in'
PASSWORD = 'Anu@8920'
COOKIES = {
    'CSRF3-Token': '1724957304.in81tFHZ0OQ3sGh3',
    '__204u': '1427207031-1724093304324',
    'usprivacy': '1---',
    'OneTrustWPCCPAGoogleOptOut': 'false',
    '_ga': 'GA1.1.222438600.1724093417',
    '_gcl_au': '1.1.192117631.1724093417',
    'IR_PI': 'e082fbb8-5e5b-11ef-8197-25ce62c668ff%7C1724093417104',
    'FPID': 'FPID2.2.NzjLE5zrzbx7HZYp%2FO%2BUv8HBXWY20CLY0WzUZUBvgRI%3D.1724093417',
    'CAUTH': 'tKjrt0hssJIz2py_u8yL6rGJ-cJN9N6frPFxIdDvCtJfCwiL6KpWA5sYHBxDGapF0V21pgF8qri3AtyWepfYIA.3wTLJGVV93MY2Myi6xdM0g.dJu8pcKZFuXhWCcGqfiRaJF6lnpRr0o9FoZE7y46GyHF1BwnbX8qSSIkZy_YvqVjoGbC2AnIbnAAk0zy7IvMOuJkZ9xfOD4LfJ60vgmqeZn712amxGji7jmsmDsW7ZBvo5pSYVmCw3bS06U-peOreIDepcQILeT7wGV4h4uHM1sxffZo7MzsNfWaKefoIOwZc-ujcC8fAPMkbUrnYtA1GYtRZAefUgGlWfzVtjb6PPhZX-4q2xUvjQ4-GDV9Onx_39l-3RYw2wP-vQqhxRBVdFWcS3AtfXLKsj3Xza3hLY6BLJanzfx5dZ9WjVHftFpTFoWI1TFmzboD1s-8cZMQL2AbBoK1gSluqPY8jeaK7CtuRQbVje3tm9sEpUnSm4q0K7y9ere--7O8ibXWvaUYKkEbcKjbo4E8OH4e8hgZsBfv2Tf39CNdIMUPAYzOCN_yK7Wm_sOp_MmDzQEeV-CV7Q',
    '_fbp': 'fb.1.1724093469876.914779850559660387',
    '_gcl_aw': 'GCL.1724193396.CjwKCAjw_ZC2BhAQEiwAXSgClsrLdOdpLMHLXDDSO0eQXth4b_xh6CdmS3zotcFTvQtxqvAeiOQDmRoCvgwQAvD_BwE',
    '_gcl_gs': '2.1.k1$i1724193394',
    'FPLC': 'ZK258cg9mxFLpX9ouj7g76K1P14IpsKM%2BUVA9U7ewxRB%2FBqmiel4RhxaFekhisV0oIdHvTHmTLJayI0IwjpEC4dtlfLnt6c3RVub%2BR2S3TcPnEy0EfJVmBsFVy65Zw%3D%3D',
    '__400v': '4f8f138a-9d59-49ae-b938-8daeaf96f8e9',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Aug+23+2024+03%3A49%3A18+GMT%2B0530+(India+Standard+Time)&version=202407.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b68f77e4-b75c-41e7-a531-919f7234b21d&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=IN%3BPB',
    'OptanonAlertBoxClosed': '2024-08-22T22:19:18.909Z',
    'IR_gbd': 'coursera.org',
    'IR_14726': '1724365159050%7C0%7C1724365159050%7C%7C',
    '_rdt_uuid': '1724093417100.40d7b512-139f-4568-bab7-ecba3ca2c093',
    'ab.storage.sessionId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9': 'g%3Aec803747-ad68-037b-1e25-46bf58027fd6%7Ce%3A1724366959111%7Cc%3A1724365159111%7Cl%3A1724365159111',
    'ab.storage.deviceId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9': 'g%3A71e336bf-8085-0f0c-b512-cc882de70630%7Ce%3Aundefined%7Cc%3A1724093307007%7Cl%3A1724365159112',
    'ab.storage.userId.6b512fd4-04b5-4fd4-8b44-3f482bc8dcf9': 'g%3A162245592%7Ce%3Aundefined%7Cc%3A1724093428416%7Cl%3A1724365159112',
    '_ga_7GZ59JSFWQ': 'GS1.1.1724365159.7.0.1724365159.0.0.393033068',
    '_ga_ZCE2Q9YZ3F': 'GS1.1.1724365159.7.0.1724365159.60.0.0',
    '_uetsid': 'a4b17f105f4411efb940afc6a3b5fc90|4y7ij2|2|foj|0|1693',
    '_tq_id.TV-63455409-1.39ed': 'bedadb0cefac299e.1724093418.0.1724365160..',
    '_uetvid': 'e0884c905e5b11ef9d59e9a382f499e6|ww10m4|1724365160477|1|1|bat.bing.com/p/insights/c/p',
    'csrftoken': 'NiR1uC7C3mYMsoMND8CCP8MV',
    '__400vt': '1724365165636',
}
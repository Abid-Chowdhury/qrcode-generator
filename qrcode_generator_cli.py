from qrcode import make
import argparse

parser = argparse.ArgumentParser('QR Code Generator')
parser.add_argument('url', help='URL to generate QR Code', type=str)
args = parser.parse_args()

def generate_qrcode(url):
    img = make(url)
    img.save('qrcode.png')

generate_qrcode(args.url)
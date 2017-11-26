import base64
import argparse


class FileEncoder:
    @staticmethod
    def encode_file_to_text(filedir, out_filename = None):
        """
        base64 encode file to text
        :param filedir: directory of file
        :param out_filename: optional output text file
        :return: (str) encoded string
        """
        f = open(filedir, "rb")
        encoded_string = base64.b64encode(f.read())
        f.close()
        if out_filename is not None:
            fout = open(out_filename, "wb")
            fout.write(encoded_string)
            fout.close()
        return encoded_string.decode("utf-8")
    @staticmethod
    def decode_text_to_file(encoded_string, out_filename):
        """

        :param encoded_string:  base64 string
        :param out_filename: output of decode file
        :return:
        """
        if out_filename is None:
            out_filename = "file.out"
        f = open(out_filename, "wb")
        decoded = base64.b64decode(encoded_string)
        f.write(decoded)
        f.close()


# if __name__=="__main__":
#     parser = argparse.ArgumentParser(description='Encode file to text')
#     parser.add_argument('-m', '--mode', help='mode', required=True)
#     parser.add_argument('-i', '--input', help='Input filename', required=True)
#     parser.add_argument('-o', '--output', help='Output filename', default=None, required=False)
#     args = parser.parse_args()
#
#     if args.mode == "encode":
#         encoded = FileEncoder.encode_file_to_text(args.input, args.output)
#         if args.output is None:
#             print(encoded)
#     elif args.mode == "decode":
#         FileEncoder.decode_text_to_file(args.input, args.output)



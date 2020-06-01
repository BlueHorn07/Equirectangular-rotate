from PIL import Image
import sys
import numpy as np
import argparse

import equirect_rotate

if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='Description of Equirect Rotate')
    parser.add_argument('file_path', type=str, help="file path")
    parser.add_argument('X', type=int, help="x rotation value")
    parser.add_argument('Y', type=int, help="y rotation value")
    parser.add_argument('Z', type=int, help="z rotation value")
    parser.add_argument('outfile_name', type=str, help='output file name')
    parser.add_argument('--isInverse', required=False, help='Inverse Transformation. True or False')
    parser.add_argument('--unit', type=str, required=False, help='degree or rad, default unit is degree')
    args = parser.parse_args()

    src_path = args.file_path
    rot_x = args.X
    rot_y = args.Y
    rot_z = args.Z

    outfile_name = args.outfile_name
    isInverse = args.isInverse
    unit = args.unit

    # open source image
    src_img = np.array(Image.open(src_path))

    out_img = equirect_rotate.Equirect_Rotate(src_img, rot_x, rot_y, rot_z, isInverse, unit)

    # save output image
    Image.fromarray(out_img).save(outfile_name)


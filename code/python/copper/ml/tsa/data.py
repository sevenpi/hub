#!/usr/bin/env python3

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
import matplotlib
from matplotlib import pyplot
from os.path import join
from pandas import read_csv
from .reader import plot_image

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------
class loader:

    matplotlib.rc( 'animation', html='html5' )
    root = '/home/clement/Desktop/data/data/tsa-kaggle'
    path_labels = 'stage1_labels.csv'
    path_zones = 'body_zones.png'
    extensions = { 1: 'aps', 2: 'a3daps' }
    
    @classmethod
    def path( cls, id, level=1 ):
        extension = cls.extensions[ level ]
        dir_ = join( cls.root, 'extract/stage1_' + extension )
        return join( dir_, id + '.' + extension )

    @classmethod
    def animate( cls, id, level=1 ):
        plot_image( cls.path( id, level ))
        pyplot.show()

    @classmethod
    def body_zones( cls ):
        path = join( cls.root, cls.path_zones )
        img = pyplot.imread( path )
        fig, ax = pyplot.subplots( figsize=( 12, 12 ))
        ax.imshow( img )
        pyplot.show()

    @classmethod
    def labels( cls ):
        path = join( cls.root, cls.path_labels )
        d = read_csv( path )
        d[ 'scan' ], d[ 'zoneid' ] = d[ 'Id' ].str.split( '_Zone', 1 ).str
        names = dict( Probability='label' )
        d = d.rename( index=str, columns=names )
        return d[[ 'scan', 'zoneid', 'label' ]]

        

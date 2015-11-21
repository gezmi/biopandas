# Authors: Sebastian Raschka <mail@sebastianraschka.com>
# License: BSD 3 clause

pdb_atomdict = [  {'id': 'record_name',
                   'line': [0, 6],
                   'type': str,
                   'strf': lambda x: '%-6s' % x},
                  {'id': 'atom_number',
                   'line': [6, 11],
                   'type': int,
                   'strf': lambda x: '%+5s' % str(x)},
                  {'id': 'blank_1',
                   'line': [11, 12],
                   'type': str,
                   'strf': lambda x: '%-1s' % x},
                  {'id': 'atom_name',
                   'line': [12, 16],
                   'type': str,
                   'strf': lambda x: ' %-3s' % x if len(x) < 4 else '%-4s' % x},
                  {'id': 'alt_loc',
                   'line': [16, 17],
                   'type': str,
                   'strf': lambda x: '%-1s' % x},
                  {'id': 'resi_name',
                   'line': [17, 20],
                   'type': str,
                   'strf': lambda x: '%-3s' % x},
                  {'id': 'blank_2',
                   'line': [20, 21],
                   'type': str,
                   'strf': lambda x: '%-1s' % x},
                  {'id': 'chain_id',
                   'line': [21, 22],
                   'type': str,
                   'strf': lambda x: '%-1s' % x},
                  {'id': 'resi_number',
                   'line': [22, 26],
                   'type': int,
                   'strf': lambda x: '%+4s' % str(x)},
                  {'id': 'resi_insert_code',
                   'line': [26, 27],
                   'type': str,
                   'strf': lambda x: '%-1s' % x},
                  {'id': 'blank_3',
                   'line': [27, 30],
                   'type': str,
                   'strf': lambda x: '%-3s' % x},
                  {'id': 'x_coord',
                   'line': [30, 38],
                   'type': float,
                   'strf': lambda x: ('%+8.3f' % x).replace('+', ' ')},
                  {'id': 'y_coord',
                   'line': [38, 46],
                   'type': float,
                   'strf': lambda x: ('%+8.3f' % x).replace('+', ' ')},
                  {'id': 'z_coord',
                   'line': [46, 54],
                   'type': float,
                   'strf': lambda x: ('%+8.3f' % x).replace('+', ' ')},
                  {'id': 'occupancy',
                   'line': [54, 60],
                   'type': float,
                   'strf': lambda x: ('%+6.2f' % x).replace('+', ' ')},
                  {'id': 'b_factor',
                   'line': [60, 66],
                   'type': float,
                   'strf': lambda x: ('%+6.2f' % x).replace('+', ' ')},
                  {'id': 'blank_4',
                   'line': [66, 72],
                   'type': str,
                   'strf': lambda x: '%-7s' % x},
                  {'id': 'segment_id',
                   'line': [72, 76],
                   'type': str,
                   'strf': lambda x: '%-3s' % x},
                  {'id': 'element_symbol',
                   'line': [76, 78],
                   'type': str,
                   'strf': lambda x: '%+2s' % x},
                  {'id': 'charge',
                   'line': [78, 80],
                   'type': float,
                   'strf': lambda x: ('%+2.1f' % x).replace('+', ' ') if pd.notnull(x) else ' '}
               ]

pdb_otherdict = [  {'id': 'record_name',
                    'line': [0, 6],
                    'type': str,
                    'strf': lambda x: x},
                   {'id': 'entry',
                    'line': [6, -2],
                    'type': str,
                    'strf': lambda x: x},
               ]

pdb_records = { 'ATOM': pdb_atomdict,
                'HETATM': pdb_atomdict,
                'ANISOU': pdb_atomdict,
                'OTHERS': pdb_otherdict
              }

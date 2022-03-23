#helper functions
import pandas as pd

def get_gt_from_file(f,gtx):
    frame= pd.DataFrame(data={'lat': f[gtx]['land_segments/latitude'][:],
                                  'lon': f[gtx]['land_segments/longitude'][:],
                                  'elev': f[gtx]['land_segments/terrain/h_te_best_fit'][:]})
    return frame

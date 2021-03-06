import os, pdb, time
import vsfm_socket_util as vsfmu

example_dir = 'examples/kermit'
os.chdir(example_dir)

path_to_vsfm_bin = '/home/nrhineha/dev/vsfm/bin/VisualSFM'
i = vsfmu.vsfm_interface(vsfm_binary_fn = path_to_vsfm_bin)

# these will send commands over sockets and not wait... VSFM will process sequentially
i.file_open_current_path()
i.view_image_thumbnails()
i.sfm_pairwise_compute_missing_match()
i.sfm_reconstruct_sparse()
i.sfm_reconstruct_dense()
i.view_dense_3d_points()

print "entering pdb REPL for additional user commands"
pdb.set_trace()
# i.close()



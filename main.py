### Importing useful packages
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D

### Run if script is run directly
if __name__ == '__main__':

	tris = np.loadtxt('tris.txt')

	edges = {
		'0': np.array([0.5, 0, 0]),
		'1': np.array([1, 0.5, 0]),
		'2': np.array([0.5, 1, 0]),
		'3': np.array([0, 0.5, 0]),

		'4': np.array([0.5, 0, 1]),
		'5': np.array([1, 0.5, 1]),
		'6': np.array([0.5, 1, 1]),
		'7': np.array([0, 0.5, 1]),

		'8': np.array([0, 0, 0.5]),
		'9': np.array([1, 0, 0.5]),
		'10': np.array([1, 1, 0.5]),
		'11': np.array([0, 1, 0.5]),
	}

	fig = plt.figure()

	ax = Axes3D(fig, auto_add_to_figure=False)
	fig.add_axes(ax)

	chunkSize = 20

	xs, ys, zs = np.indices((chunkSize, chunkSize, chunkSize))

	grid = (xs - chunkSize/2)**2 + (ys - chunkSize/2)**2 + (zs - chunkSize/2)**2 - (chunkSize/3)**2

	alphas = grid/np.max(grid)

	# ax.scatter(xs, ys, zs, c='k', alpha=alphas, s=10)
	# ax.scatter(xs, ys, zs, c='r', alpha=boolean, s=3)

	# ax.set_box_aspect([1,1,1])

	# plt.show()

	thresh = 0

	apple = True

	triXs = np.array([])
	triYs = np.array([])
	triZs = np.array([])

	for i in range(chunkSize-1):
		for j in range(chunkSize-1):
			for k in range(chunkSize-1):

				v0 = grid[i, j, k]
				v1 = grid[i+1, j, k]
				v2 = grid[i+1, j+1, k]
				v3 = grid[i, j+1, k]

				v4 = grid[i, j, k+1]
				v5 = grid[i+1, j, k+1]
				v6 = grid[i+1, j+1, k+1]
				v7 = grid[i, j+1, k+1]

				v0B = v0 > thresh
				v1B = v1 > thresh
				v2B = v2 > thresh
				v3B = v3 > thresh

				v4B = v4 > thresh
				v5B = v5 > thresh
				v6B = v6 > thresh
				v7B = v7 > thresh

				triIndex = v0B*(2**0) + v1B*(2**1) + v2B*(2**2) + v3B*(2**3) + v4B*(2**4) + v5B*(2**5) + v6B*(2**6) + v7B*(2**7)

				tri = tris[triIndex]
				mask = tri != -1.0
				tri = tri[mask].astype(int)

				if len(tri) > 0:

					for l in range(len(tri)//3):

						offset = np.array([i, j, k])

						ea = offset + edges[str(tri[3*l])]
						eb = offset + edges[str(tri[3*l+1])]
						ec = offset + edges[str(tri[3*l+2])]

						es = np.array([ea, eb, ec])

						x, y, z = es.transpose()

						triXs = np.concatenate((triXs, x))
						triYs = np.concatenate((triYs, y))
						triZs = np.concatenate((triZs, z))

						verts = [list(zip(x, y, z))]

						collection = Poly3DCollection(verts)

						ax.add_collection3d(collection)

	# verts = [list(zip(triXs, triYs, triZs))]

	# collection = Poly3DCollection(verts)

	# ax.add_collection3d(collection)
	# face_color = [1, 1, 1]
	# collection.set_facecolor(face_color)
	# collection.set_edgecolor('k')

	ax.set_xlim(0, chunkSize)
	ax.set_ylim(0, chunkSize)
	ax.set_zlim(0, chunkSize)

	ax.set_box_aspect([1, 1, 1])

	plt.show()



	# print(tris)
import torch


class KeypointTransform(torch.nn.Module):

    def __init__(self, scale_x=1., scale_y=1.):
        super().__init__()
        self.scale_x = scale_x
        self.scale_y = scale_y

    def set_scale(self, scale_x=1., scale_y=1.):
        self.scale_x = scale_x
        self.scale_y = scale_y

    def forward(self, points):
        raise NotImplementedError()

class KeypointScale(KeypointTransform):

    def __init__(self, scale_x=1., scale_y=1.):
        super().__init__(scale_x, scale_y)

    def forward(self, points):
        points_ = points.clone()
        points_[:, :, 0] *= self.scale_x
        points_[:, :, 1] *= self.scale_y
        return points_

class KeypointNormalization(KeypointTransform):

    def __init__(self, scale_x=1., scale_y=1.):
        super().__init__(scale_x, scale_y)

    def forward(self, points):
        points_ = points.clone()
        # normalization the way DECA uses it.
        # the keypoints are not used in image space but in normalized space
        # for loss computation
        # the normalization is as follows:
        points_[:, :, 0] -= self.scale_x/2
        points_[:, :, 0] /= self.scale_x/2
        points_[:, :, 1] -= self.scale_y/2
        points_[:, :, 1] /= self.scale_y/2
        return points_

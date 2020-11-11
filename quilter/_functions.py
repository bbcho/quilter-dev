from functools import wraps # This convenience func preserves name and docstring
import matplotlib
import matplotlib.pyplot as plt

def _add_method(cls):
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
        return func # returning func means func can still be used normally
    return decorator


# override __add__ method in Figure object
@_add_method(matplotlib.figure.Figure)
def __add__(self, fig2):
    # load ax from first fig
    ax_list_1 = self.axes

    # load ax from second fig
    ax_list_2 = fig2.axes

    ax_list = ax_list_1 + ax_list_2
    n = len(ax_list)

    fig, ax = plt.subplots(n,1) 

    # create new figure with subplots
    for i, ax_i in enumerate(ax_list):
        ax[i] = ax_i

    # return figure
    return fig, ax




if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    import pickle
    import io

    num_rows = 10
    num_cols = 1
    fig, axs = plt.subplots(num_rows, num_cols, sharex=True)
    for i in range(num_rows):
        ax = axs[i]
        ax.plot(np.arange(10), np.arange(10)**i)

    def on_click(event):

        if not event.inaxes: return
        inx = list(fig.axes).index(event.inaxes)
        buf = io.BytesIO()
        pickle.dump(fig, buf)
        buf.seek(0)
        fig2 = pickle.load(buf) 

        for i, ax in enumerate(fig2.axes):
            if i != inx:
                fig2.delaxes(ax)
            else:
                axes=ax

        axes.change_geometry(1,1,1)
        fig2.show()

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()
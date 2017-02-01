from nltk.metrics import NgramAssocMeasures

class QuadgramAssocMeasures(NgramAssocMeasures):
    """
    A collection of quadgram association measures. Each association measure
    is provided as a function with four arguments::

    quadgram_score_fn(n_iiii,
                (n_iiix, n_iixi, n_ixii, n_xiii),
                (n_iixx, n_ixix, n_ixxi, n_xiix, n_xixi, n_xxii),
                (n_ixxx, n_xixx, n_xxix, n_xxx,i),
                n_xxxx)
      
    The arguments constitute the marginals of a contingency table, counting
    the occurrences of particular events in a corpus. The letter i in the
    suffix refers to the appearance of the word in question, while x indicates
    the appearance of any word. Thus, for example:
    n_iiii counts (w1, w2, w3, w4), i.e. the quadgram being scored
    n_ixxx counts (w1, *, *, *)
    n_xxxx counts (*, *, *, *), i.e. any quadgram
    """
    _n = 4
    
    @staticmethod
    def _contingency(n_iiii, 
                     n_iiix_tuple,
                     n_iixx_tuple,
                     n_ixxx_tuple,
                     n_xxxx):

        """Calculates values of a quadgram contingency table (or cube) from marginal
        values.
        """
        (n_iiix, n_iixi, n_ixii, n_xiii) = n_iiix_tuple
        (n_iixx, n_ixix, n_ixxi, n_xixi, n_xxii, n_xiix) = n_iixx_tuple
        (n_ixxx, n_xixx, n_xxix, n_xxxi) = n_ixxx_tuple

        n_iiio = n_iiix - n_iiii
        n_iioi = n_iixi - n_iiii
        n_ioii = n_ixii - n_iiii
        n_oiii = n_xiii - n_iiii
        
        n_iioo = n_iixx - n_iiii - n_iioi - n_iiio
        n_ioio = n_ixix - n_iiii - n_iiio - n_ioii
        n_iooi = n_ixxi - n_iiii - n_ioii - n_iioi
        n_oiio = n_xiix - n_iiii - n_oiii - n_iiio
        n_oioi = n_xixi - n_iiii - n_oiii - n_iioi
        n_ooii = n_xxii - n_iiii - n_oiii - n_ioii
        
        n_iooo = n_ixxx - n_iiii - n_iioi - n_iiio - n_iioo - n_ioii - n_iooi - n_ioio
        n_oioo = n_xixx - n_iiii - n_iioi - n_iiio - n_iioo - n_oiii - n_oioi - n_oiio
        n_ooio = n_xxix - n_iiii - n_iiio - n_ioii - n_ioio - n_oiii - n_oiio - n_ooii
        n_oooi = n_xxxi - n_iiii - n_iioi - n_ioii - n_iooi - n_oiii - n_oioi - n_ooii
        n_oooo = n_xxxx - n_iiii - n_oooi - n_ooio - n_oioo - n_iooo - n_ooii - n_oioi - n_oiio - n_iooi - n_ioio - n_iioo - n_iiio - n_iioi - n_ioii - n_oiii   
        
        return (n_iiii, 
                n_oiii, n_ioii, n_iioi, n_iiio, 
                n_iioo, n_ioio, n_iooi, n_oiio, n_oioi, n_ooii, 
                n_iooo, n_oioo, n_ooio, n_oooi, n_oooo)
    
    @staticmethod
    def _marginals(*contingency):
        """Calculates values of contingency table marginals from its values."""
        n_iiii, n_oiii, n_ioii, n_iioi, n_iiio, n_iioo, n_ioio, n_iooi, n_oiio, n_oioi, n_ooii, n_iooo, n_oioo, n_ooio, n_oooi, n_oooo = contingency
        return (n_iiii,
                (n_iiii + n_iiio, 
                 n_iiii + n_iioi, 
                 n_iiii + n_ioii, 
                 n_iiii + n_oiii),
                (n_iioo + n_iiii + n_iioi + n_iiio,
                n_ioio + n_iiii + n_iiio + n_ioii,
                n_iooi + n_iiii + n_ioii + n_iioi,
                n_oiio + n_iiii + n_oiii + n_iiio,
                n_oioi + n_iiii + n_oiii + n_iioi,
                n_ooii + n_iiii + n_oiii + n_ioii),
                (n_iooo + n_iiii + n_iioi + n_iiio + n_iioo + n_ioii + n_iooi + n_ioio,
                n_oioo + n_iiii + n_iioi + n_iiio + n_iioo + n_oiii + n_oioi + n_oiio,
                n_ooio + n_iiii + n_iiio + n_ioii + n_ioio + n_oiii + n_oiio + n_ooii,
                n_oooi + n_iiii + n_iioi + n_ioii + n_iooi + n_oiii + n_oioi + n_ooii),
                sum(contingency))
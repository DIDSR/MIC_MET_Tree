# tree/nodes/n12_multi_score.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_score = get_image_base64(f"{IMG_BASE_PATH}G12kClass_scourOutput_figC.jpg")
_img_prob  = get_image_base64(f"{IMG_BASE_PATH}G12kClass_probOutput_figC.jpg")

def _img_tag(img_b64, alt):
    if img_b64:
        return (f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="data:image/jpeg;base64,{img_b64}" alt="{alt}" '
                f'style="max-width:100%;height:auto;border:1px solid #ddd;'
                f'border-radius:4px;padding:5px;"></div>')
    return '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_score_img_tag = _img_tag(_img_score, "Figure: example score output for a k-class classifier")
_prob_img_tag  = _img_tag(_img_prob,  "Figure: Example probability output for a k-class classifier")

_OVERVIEW = f"""
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
       <p style="color: #333; line-height: 1.6;">Based on your answers, your task is a <i>multi-class</i> classification task, based on a <i>reference standard with negligible variability</i>, and returns a score output for each input (see the figure below for an example output). The evaluation metrics used for this type of classification task are typically generalized from those for a binary classification with similar context. You may choose a metric/method that you are interested in from the list at the bottom to learn more about it. To proceed, it may be helpful to familiarize yourself with the following notations, which may be used in the subsequent nodes.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notations used in nodes below</h3>
       <p style="color: #333; line-height: 1.6;">For a <i>k-class classifier with score output</i>, we use the following notation. Given a dataset,</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><i>m</i> denotes the total number of cases/observations/subjects in the dataset,</li>
         <li><i>k</i> denotes the number of classes,</li>
         <li><i>m</i><sub style="font-size: 0.75em;">j</sub> denotes the number of cases of class <i>j</i>.</li>
         <li><i>p</i>(<i>j</i>) denotes the probability of classes <i>j</i>, i.e.,</li>
         <li>For the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation in the dataset, the score output of a <i>k-class classifier</i> is denoted as (score<sub style="font-size: 0.75em;">i1</sub>, score<sub style="font-size: 0.75em;">i2</sub>, ...score<sub style="font-size: 0.75em;">ik</sub>), where score<sub style="font-size: 0.75em;">ij</sub> stands for the score predicted by the classifier for the <i>i</i><sup style="font-size: 0.7em;">th</sup> observation belonging to the <i>j</i><sup style="font-size: 0.7em;">th</sup> class (<i>i</i>= 1, ..., <i>m</i>, <i>j</i>=1, ...,<i>k</i>), as shown in the figure below.</li>
       </ul>
     </section>
     {_score_img_tag}
     <p style="color: #666; margin-top: 1rem; font-style: italic; text-align: center;">Figure: example score output for a <i>k</i>-class classifier</p>
"""

_AUC_ONE_VS_REST = """
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Fawcett (2006) described an AUC measure for <i>k-class classification</i>, which is a weighted average of AUC for each individual class against the rest weighted by the a priori probability of each class, treating <i>k-class classifier</i> as <i>k</i> two-class classifiers.</li>
         <li>This measure is also referred to as <i>AUC of each class against the rest, using the a priori class distribution</i>, abbreviated as AUNP in Ferri et al. (2009).</li>
         <li>Ferri et al. (2009) described another AUC measure, referred to as <i>AUC of each class against the rest, using the uniform distribution</i>, abbreviated as AUNU, which is an <i>unweighted</i> version of AUNP. Details below.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
       <p style="color: #333; line-height: 1.6;">Weighted AUC of each class vs. the other classes combined (referred to as AUNP (Ferri et al., 2009)) is defined as</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           AUNP = <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <i>p</i>(<i>j</i>) &#183; AUC(<i>j</i>, rest<sub style="font-size: 0.7em;">j</sub>)
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">where <i>p</i>(<i>j</i>) is the true class probability, and AUC(<i>j</i>, rest<sub style="font-size: 0.7em;">j</sub>) is the AUC defined for binary classifiers, treating <i>j</i><sup style="font-size: 0.7em;">th</sup> class as one class, and all the other classes combined as the other class.</p>
       <p style="color: #333; line-height: 1.6;">Unweighted AUC of each class vs. the other classes combined (referred to as AUNU (Ferri et al., 2009)) is defined as</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           AUNU = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> AUC(<i>j</i>, rest<sub style="font-size: 0.7em;">j</sub>)
         </span>
       </p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>The weighted version of this measure (AUNP) is affected by the estimate of class probability <i>p&#770;</i>(<i>j</i>). One needs to be cautious to select AUNP as the performance metric if <i>p&#770;</i>(<i>j</i>) derived from the dataset is not representative of the true class probability <i>p</i>(<i>j</i>).</li>
         <li>The unweighted version of this measure (AUNU) is also affected by class prevalence.</li>
         <li>We recommend that users report all individual AUC(<i>j</i>, rest<sub style="font-size: 0.7em;">j</sub>) (<i>j</i> = 1 ,..., <i>k</i>) together with the averaged AUC measure.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Fawcett, T. (2006). An introduction to ROC analysis. Pattern recognition letters, 27(8), 861-874.</li>
         <li>Ferri, C., Hernandez-Orallo, J., &amp; Modroiu, R. (2009). An experimental comparison of performance measures for classification. Pattern Recognition Letters, 30(1), 27-38.</li>
       </ul>
     </section>
"""

_AUC_ONE_VS_ONE = """
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Hand and Till (2001) described an AUC measure for <i>k-class classification</i> which is an average of AUC for <i>k</i>(<i>k</i> - 1) pairwise binary classifiers. This measure is also referred to by Ferri et al. (2009) as <i>AUC of each class against each other, using the uniform class distribution</i>, abbreviated as AU1U.</li>
         <li>Ferri et al. (2009) described another AUC measure, referred to as <i>AUC of each class against each other, using the a priori distribution</i>, abbreviated as AU1P, which is the <i>weighted</i> version of AU1U. Details are below.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
       <p style="color: #333; line-height: 1.6;">Unweighted AUC of each class vs. each of the other <i>k</i>-1 classes (referred to as AU1U (Ferri et al., 2009)) is defined as</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           AU1U = (1/[<i>k</i>(<i>k</i>-1)]) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.55em; vertical-align: sub; margin-left: -0.3rem;"><i>l</i>=1, <i>l</i>&#8800;<i>j</i></sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> AUC(<i>j</i>, <i>l</i>)
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">where AUC(<i>j</i>, <i>l</i>) is the AUC defined for binary classifiers, treating <i>j</i><sup style="font-size: 0.7em;">th</sup> class as one class, and <i>l</i><sup style="font-size: 0.7em;">th</sup> class as the other class.</p>
       <p style="color: #333; line-height: 1.6;">Weighted AUC of each class vs. each of the other <i>k</i>-1 classes (referred to as AU1P (Ferri et al., 2009)) is defined as</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           AU1P = (1/[<i>k</i>(<i>k</i>-1)]) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.55em; vertical-align: sub; margin-left: -0.3rem;"><i>l</i>=1, <i>l</i>&#8800;<i>j</i></sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <i>p</i>(<i>j</i>) &#183; AUC(<i>j</i>, <i>l</i>)
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">where <i>p</i>(<i>j</i>) is the true class probability.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>The weighted version of this measure, AU1P, is affected by the estimate of class probability <i>p&#770;</i>(<i>j</i>). One needs to be cautious to select AU1P as the performance metric if <i>p&#770;</i>(<i>j</i>) derived from the dataset is not representative of the true class probability <i>p</i>(<i>j</i>).</li>
         <li>We recommend users report all individual AUC(<i>j</i>, <i>l</i>) (<i>j</i>, <i>l</i> = 1, ..., <i>k</i>, <i>j</i> &#8800; <i>l</i>) together with the averaged AUC measure.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Hand, D.J., Till, R.J. (2001). A simple generalization of the area under the ROC curve to multiple class classification problems. Mach. Learning 45 (2), 171&#8211;186.</li>
         <li>Ferri, C., Hernandez-Orallo, J., &amp; Modroiu, R. (2009). An experimental comparison of performance measures for classification. Pattern Recognition Letters, 30(1), 27-38.</li>
       </ul>
     </section>
"""

_MAPR = (
    """
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
       <p style="color: #333; line-height: 1.6;">In this node, we introduce a performance metric for <i>k-class classification</i> with a <i>probability</i> output, which can be regarded as a special case of a <i>score</i> output.</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Mitchell (1997) described a measure for <i>k-class classification</i> with a probability score output, which is an average of mean predicted probabilities for each class. This measure is also referred to by Ferri et al. (2009) as <i>macro average mean probability rate (MAPR)</i>.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notation</h3>
       <p style="color: #333; line-height: 1.6;">In this node, we use the following mathematical notation. For the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation in the dataset, the probability output of a <i>k-class classifier</i> is denoted as (<i>p</i><sub style="font-size: 0.75em;">i1</sub>, <i>p</i><sub style="font-size: 0.75em;">i2</sub>, ...<i>p</i><sub style="font-size: 0.75em;">ik</sub>) where <i>p</i><sub style="font-size: 0.75em;">ij</sub> stands for the probability predicted by the classifier for the <i>i</i><sup style="font-size: 0.7em;">th</sup> observation belonging to the <i>j</i><sup style="font-size: 0.7em;">th</sup> class, <i>i</i> = 1, ...<i>m</i>, <i>j</i> = 1, ..., <i>k</i>, as shown in the figure below.</p>
     </section>
    """
    + _prob_img_tag
    + """
     <p style="color: #666; margin-top: 1rem; font-style: italic; text-align: center;">Figure: Example probability output for a <i>k</i>-class classifier</p>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
       <p style="color: #333; line-height: 1.6;">The <i>macro average mean probability rate (MAPR)</i> is defined as (Ferri et al., 2009)</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           MAPR = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> [(1/<i>m</i><sub style="font-size: 0.7em;">j</sub>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>m</i></sup> <i>I</i>&#123;true class of <i>i</i> = <i>j</i>&#125; &#183; <i>p</i><sub style="font-size: 0.7em;">ij</sub>]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">where <i>k</i> is the number of classes, <i>m</i><sub style="font-size: 0.75em;">j</sub> is the number of cases in class <i>j</i>, <i>m</i> is the number of cases in the dataset, <i>I</i>&#123;.&#125; is the indicator function that take the value of 1 if true and 0 if false, and <i>p</i><sub style="font-size: 0.75em;">ij</sub> is the probability output described in the example output figure above.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>We can regard MAPR as a generalization of balanced accuracy from the case of class output to the case of probability output in a multi-class classification problem.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Mitchell, T.M. (1997). Machine Learning. McGraw-Hill.</li>
         <li>Ferri, C., Hernandez-Orallo, J., &amp; Modroiu, R. (2009). An experimental comparison of performance measures for classification. Pattern Recognition Letters, 30(1), 27-38.</li>
       </ul>
     </section>
"""
)

NODE = {
    "id": "N1_2",
    "title": "Multi-Class Classification: Metrics generalized from binary classification for score output",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "AUC of each class vs. the other classes combined (weighted and unweighted)": {
            "html": _AUC_ONE_VS_REST, "latex": []},
        "AUC of each class vs. each of the other k-1 classes (weighted and unweighted)": {
            "html": _AUC_ONE_VS_ONE, "latex": []},
        "Macro Average Mean Probability Rate (MAPR)": {
            "html": _MAPR, "latex": []},
    },
}

# tree/nodes/n13_multi_topn.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_topn = get_image_base64(f"{IMG_BASE_PATH}G13kClass_topnLabel_figC.jpg")

def _img_tag(img_b64, alt):
    if img_b64:
        return (f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="data:image/jpeg;base64,{img_b64}" alt="{alt}" '
                f'style="max-width:100%;height:auto;border:1px solid #ddd;'
                f'border-radius:4px;padding:5px;"></div>')
    return '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_OVERVIEW = f"""
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
       <p style="color: #333; line-height: 1.6;">Based on your answers, your task is a <i>multi-class</i> classification task, based on a <i>reference standard with negligible variability</i>, and returns an output of <i>n</i> most likely labels for each input (see the figure below for an example output). A typical evaluation metric used for this type of classification task is top-<i>n</i>-accuracy. You may choose a metric from the list at the bottom to learn more about it.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notations</h3>
       <p style="color: #333; line-height: 1.6;">For the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation, the output of the <i>k</i>-class classifier in this branch is a vector of <i>n</i> class labels, corresponding to the <i>n</i> most likely classes predicted for the observation, denoted by (&#375;<sub style="font-size: 0.75em;">i1</sub>, &#375;<sub style="font-size: 0.75em;">i2</sub>, ..., &#375;<sub style="font-size: 0.75em;">in</sub>), as shown in the figure below.</p>
     </section>
     {_img_tag(_img_topn, "Figure: example output of top-n-class labels")}
     <p style="color: #666; margin-top: 1rem; font-style: italic; text-align: center;">Figure: example output of top-<i>n</i>-class labels for the <i>i</i><sup style="font-size: 0.7em;">th</sup> case corresponding to the <i>n</i> most likely classes</p>
"""

_TOPN = """
     <section style="margin-top: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Top-<i>n</i>-accuracy</h3>
       <h4 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h4>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>For some tasks in <i>k</i>-class classification problem, it is more favorable to provide an output of the multiple, say, <i>n</i>, most likely class labels to the users instead of a single one.</li>
         <li>For example, a search engine often provides users with several alternative results within the first page, so users can choose the one that fits their needs best from amongst multiple options.</li>
         <li>Another example is an online shopping system that recommends to customers several products that they are potentially interested in, instead of a single item.</li>
         <li>Top <i>n</i> accuracy is an accuracy metric used for multi-class classification that returns an output of a vector of <i>n</i> most likely class labels, instead of just a single label, for each case in the dataset.</li>
         <li>Please note: This section assumes that the <i>n</i> class labels that are output do not necessarily form a ranked list and that the order of the class labels for this metric is not relevant.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h4 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h4>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>The output for each case in the dataset would be an <i>n</i>-dimensional vector, which represents top <i>n</i> most likely labels that the case is predicted to belong to.</li>
         <li>The <i>n</i>-dimensional output of the classifier for the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation in the dataset, (&#375;<sub style="font-size: 0.75em;">i1</sub>, ..., &#375;<sub style="font-size: 0.75em;">iz</sub>, ..., &#375;<sub style="font-size: 0.75em;">in</sub>), denotes the <i>n</i> most likely classes predicted by the classifier for the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation, <i>i</i> = 1, ..., <i>m</i>, <i>j</i> = 1, ..., <i>n</i>, where <i>n</i> &lt; <i>k</i> is a pre-specified number.</li>
         <li><i>y</i><sub style="font-size: 0.75em;">i</sub> denotes the true class label for the <i>i</i><sup style="font-size: 0.7em;">th</sup> case.</li>
         <li>Following Wang &amp; Deng (2013), top <i>n</i> accuracy can be calculated as:
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               Top-<i>n</i> accuracy = (1/<i>m</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>m</i></sup> <i>I</i>{<i>y</i><sub style="font-size: 0.7em;">i</sub> &#8712; (&#375;<sub style="font-size: 0.7em;">i1</sub>, ..., &#375;<sub style="font-size: 0.7em;">in</sub>)}
             </span>
           </p>
           <p style="color: #333; line-height: 1.6;">where <i>m</i> is the number of observations in the dataset and <i>I</i>{.} is the indicator function that takes value of 1 if true and 0 is false.</p>
         </li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h4 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes</h4>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>When <i>n</i>=1, top-1 accuracy is the overall accuracy.</li>
         <li>This metric can be affected by whether the class prevalences in a test dataset are representative of the class prevalences in the intended population, and should be used carefully, especially for imbalanced datasets.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h4 style="font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h4>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Wang, S. H., &amp; Deng, Z. H. (2013). Semantic Inversion in XML Keyword Search with General Conditional Random Fields. In International Conference on Web Information Systems Engineering (pp. 431-440). Springer, Berlin, Heidelberg.</li>
       </ul>
     </section>
"""

NODE = {
    "id": "N1_3",
    "title": "Multi-Class Classification: Metrics based on n most likely label outputs",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "Top-n accuracy": {"html": _TOPN, "latex": []},
    },
}

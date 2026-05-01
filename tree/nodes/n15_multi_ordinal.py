# tree/nodes/n15_multi_ordinal.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_weights = get_image_base64(f"{IMG_BASE_PATH}G15kClass_ordinal_figC.jpg")
_img_table1  = get_image_base64(f"{IMG_BASE_PATH}G15kClass_ordinal_ConfusionTab_figC.jpg")

def _img_tag(img_b64, alt):
    if img_b64:
        return (f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="data:image/jpeg;base64,{img_b64}" alt="{alt}" '
                f'style="max-width:100%;height:auto;border:1px solid #ddd;'
                f'border-radius:4px;padding:5px;"></div>')
    return '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_OVERVIEW = """
  <div style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;"> Multi-Class Classification: Metrics based on level of measurement</h2>
   <p style="color: #333; line-height: 1.6;">Based on your answers, your task is a <i>multi-class ordinal classification</i> task, based on a <i>reference standard with negligible variability</i>, and returns a single label output for each input. Currently, there is a lack of widely acknowledged performance evaluation metric used for this context. Please read the following for a summary of evaluation metrics/methods applicable to this scenario.</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Evaluation metrics/approaches for ordinal classification</h2>
   <p style="color: #dc2626; font-weight: bold; line-height: 1.6;">Highlight message</p>
   <p style="color: #333; line-height: 1.6;">Evaluation of classification models often relies on a perfect ground truth, which may not be available in many real-world scenarios. This leads to truth variability which poses a challenge for evaluating classification tasks. In this discussion, we present three (but not all) approaches&#8212;percent agreement metrics, interchangeability metric, and latent class analysis&#8212;to address this issue. It is important to note that no universally accepted evaluation metric exists for classification tasks with truth variability, and the presented approaches are intended as starting points to explore this area. However, it is essential to remember that these methods should not replace the gold standard test, which remains the ideal reference standard for evaluation.</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
   <p style="color: #333; line-height: 1.6;">Classification tasks can be categorized into nominal classification, where the outcome can be categorized but not ranked, and ordinal classification, where the outcome can be categorized and ranked and the intervals between neighboring ranks may or may not be equal (e.g., diagnosing patients as normal or mildly/moderately/severely diseased). Existing studies (e.g. Ferri et al., 2009) on classification evaluation metrics mostly focus on nominal classification, with fewer studies addressing ordinal classification. To our knowledge, there is no consensus approach about evaluation metrics for ordinal classification tasks. We try to group some (but not all) the existing solutions into several categories in related work section below.</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Related work</h3>
   <p style="color: #333; line-height: 1.6;">One naive approach is to use evaluation metrics designed for nominal classification directly or with modifications to evaluate ordinal classification. The former treats ordinal scale as nominal and ignores its ordinal nature, while the latter incorporates ordinality into the modification. Weighted Cohen's Kappa is one notable metric in this category. We introduce this metric in the section 'Example metric: weighted Cohen's Kappa' below. Sakai (2021) reviewed 9 metrics for ordinal classification tasks and recommended linearly weighted kappa as the primary measure if the task does not involve multiple runs that always return the same class. Nonetheless, this does not necessarily mean that weighted kappa is the best metric, as Sakai's work did not cover all metrics (such as Kendall's Tau) and there is some controversy about the original Cohen's kappa (Guggenmoos-Holzmann, 1996).</p>
   <p style="color: #333; line-height: 1.6;">Another approach involves modifying evaluation metrics for continuous variables to assess ordinal data by assigning fixed values to each ordinal category and then computing error metrics designed for continuous outcomes. However, this approach ignores the fact that an ordinal scale may not be an interval scale (Amigo et al., 2020). Two example metrics in this type are modified mean absolute error (MAE) and mean square error (MSE).</p>
   <p style="color: #333; line-height: 1.6;">A third approach involves using ranking-based metrics that consider the ordinal relation in the data without focusing on exact values. Examples of such metrics include Kendall's Tau coefficient (&#964;) (Kendall, 1938), prediction probability (Smith et al., 1996), Gamma, and Somer's d (Agresti, 2010). These metrics are based on the number of concordant and discordant pairs of observations, respecting the ordinal nature of the data without imposing an interval scale. Kendall's Tau was used as part of the evaluation criteria in Sakai (2020)'s review of 9 metrics, and prediction probability was employed as a performance metric in the Breast Pathology Quantitative Biomarkers Challenge (Petrick et al., 2021). However, more studies with rigorous validation designs are necessary to determine if this approach outperforms the others.</p>
   <p style="color: #333; line-height: 1.6;">Apart from these three approaches, there may be other types of evaluation methods for ordinal classification tasks, such as the model-based approach described by Agresti (2010). This approach summarizes the association between two ordinal variables by reducing the kxk confusion table to (k-1)x(k-1) odds ratios, and then reducing these odds ratios to a single number summary by fitting a model that assumes a common value for all odds ratios of a particular type. The selection of the fitted model and the measures of association can vary within this approach, offering numerous possibilities. We thus do not delve into this approach in detail here. Interested readers can refer to Delfino et al.'s (2022) work for an example of this approach applied to comparing two ordinal classifiers.</p>
   <p style="color: #333; line-height: 1.6;">It is important to note that each approach in existing studies has its flaws to varying degrees. By providing information about these options, our aim is to offer a starting point for users to investigate the best option for their specific needs, rather than making a specific recommendation. Currently, there is no single universally accepted evaluation metric for ordinal classification.</p>
   <p style="color: #333; line-height: 1.6;">Next, we describe some example metrics mentioned above.</p>
  </div>
"""

_WEIGHTED_KAPPA = (
    """
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">An example metric for the first approach: weighted Cohen's Kappa</h3>
   <p style="color: #333; line-height: 1.6;">The general form of Cohen's Kappa is given below, which is shared by both the unweighted version for nominal variables and the weighted version for ordinal variables</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     &#954; = (p<sub style="font-size: 0.7em;">o</sub> &#8722; p<sub style="font-size: 0.7em;">e</sub>) / (1 &#8722; p<sub style="font-size: 0.7em;">e</sub>)
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where p<sub style="font-size: 0.75em;">o</sub> is the proportion of observed agreement among raters, p<sub style="font-size: 0.75em;">e</sub> is the hypothetical probability of expected chance agreement. The explicit form of weighted Cohen's Kappa for ordinal variables can be obtained by plugging these weighted p<sub style="font-size: 0.75em;">o</sub> and p<sub style="font-size: 0.75em;">e</sub> in the general form, which is given below (Fleiss et al., 1969).</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 0.95rem; line-height: 2;">
     p<sub style="font-size: 0.7em;">o</sub> = <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup>
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup>
     <i>w</i><sub style="font-size: 0.7em;">ij</sub> <i>p</i><sub style="font-size: 0.7em;">ij</sub>
     <br><br>
     p<sub style="font-size: 0.7em;">e</sub> = <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup>
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup>
     <i>w</i><sub style="font-size: 0.7em;">ij</sub> <i>p</i><sub style="font-size: 0.7em;">i+</sub> <i>p</i><sub style="font-size: 0.7em;">+j</sub>
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li><i>w</i><sub style="font-size: 0.75em;">ij</sub> is the weight assigned to the (<i>i</i>, <i>j</i>)<sup style="font-size: 0.7em;">th</sup> cell in the confusion matrix,</li>
    <li><i>p</i><sub style="font-size: 0.75em;">ij</sub> = <i>n</i><sub style="font-size: 0.75em;">ij</sub>/<i>N</i> is the observed proportion of subjects placed in the (<i>i</i>, <i>j</i>)<sup style="font-size: 0.7em;">th</sup> cell in the confusion matrix,</li>
    <li><i>p</i><sub style="font-size: 0.75em;">i+</sub> = <i>n</i><sub style="font-size: 0.75em;">i+</sub>/<i>N</i> is the proportion of subjects placed in the <i>i</i><sup style="font-size: 0.7em;">th</sup> row in the confusion matrix,</li>
    <li><i>p</i><sub style="font-size: 0.75em;">+j</sub> = <i>n</i><sub style="font-size: 0.75em;">+j</sub>/<i>N</i> is the proportion of subjects placed in the <i>j</i><sup style="font-size: 0.7em;">th</sup> column in the confusion matrix.</li>
   </ul>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Linear weight and quadratic weight</h3>
   <p style="color: #333; line-height: 1.6;">There are two commonly used weighting system for computing weighted Cohen's Kappa in the literature (note that, however, there can be other weight choices too).</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Linear weight, also known as Cicchetti-Allison weights to name after the authors (Cicchetti and Allison, 1971), which changes linearly regarding distance |<i>i</i>-<i>j</i>|.</li>
    <li>Quadratic weight: also known as Fleiss-Cohen weights to name after the authors (Fleiss and Cohen, 1973), which changes quadratically regarding distance |<i>i</i>-<i>j</i>|.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion Matrix for <i>k</i>-class classification problem</p>
    """
    + _img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")
    + """
   <p style="color: #333; line-height: 1.6;">For a <i>k</i>x<i>k</i> confusion table as shown in Table 1, the linear weight for a given cell is:</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     <i>w</i><sub style="font-size: 0.7em;">ij</sub> = 1 &#8722; |<i>i</i>&#8722;<i>j</i>| / (<i>k</i>&#8722;1)
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">The quadratic weight for a given cell is:</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     <i>w</i><sub style="font-size: 0.7em;">ij</sub> = 1 &#8722; [(<i>i</i>&#8722;<i>j</i>) / (<i>k</i>&#8722;1)]&#178;
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where |<i>i</i>-<i>j</i>| is distance between two categories, <i>k</i> is the number of classes in the classification task. Both linear and quadratic weight schemes give full credit 1 for full agreements (i.e., distance |<i>i</i>-<i>j</i>|=0), zero credit for maximum disagreement (e.g., <i>i</i>=0 <i>j</i>=<i>k</i>), and partial credit for partial agreement (i.e., 2 different, but close categories). The difference is that linear weight changes linearly regarding distance |<i>i</i>-<i>j</i>|, while quadratic weight changes quadratically (see figure 1). This quadratic change results in higher partial credits than linear weights and thus a more "forgiving" scheme, as quadratic weight amplifies the larger differences.</p>
    """
    + _img_tag(_img_weights, "Figure 1: comparison of linear vs. quadratic weights")
    + """
   <p style="color: #666; margin-top: 1rem; font-style: italic; text-align: center;">Figure 1. comparison of linear vs. quadratic weights, 4-class classification</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Cicchetti, D. V., &amp; Allison, T. (1971). A new procedure for assessing reliability of scoring EEG sleep recordings. American Journal of EEG Technology, 11(3), 101-110.</li>
    <li>Fleiss, J. L., &amp; Cohen, J. (1973). Educational and Psychological Measurement. Educational and Psychological Measurement, 33(3), 613-619.</li>
    <li>Fleiss, J. L., Cohen, J., &amp; Everitt, B. S. (1969). Large sample standard errors of kappa and weighted kappa. Psychological bulletin, 72(5), 323.</li>
    <li>Guggenmoos-Holzmann, I. (1996). The meaning of kappa: probabilistic concepts of reliability and validity revisited. Journal of clinical epidemiology, 49(7), 775-775.</li>
    <li>Sakai, T. (2021). Evaluating evaluation measures for ordinal classification and ordinal quantification. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 2759-2769).</li>
   </ul>
  </div>
"""
)

_MAE_MSE = """
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Example metrics for the second approach: mean absolute error (MAE) or mean square error (MSE)</h3>
   <p style="color: #333; line-height: 1.6;">Another commonly seen option is using error metrics designed for a continuous outcome, such as mean absolute error (MAE) or mean square error (MSE), to assess ordinal classification performance, by converting ordinal outcome to pre-defined numeric values. Such a conversion may assume two adjacent ordinal values as equally distanced. For example, an ordinal outcome with 4 possible values such as normal or mildly/moderately/severely diseased may be encoded as 1/2/3/4. One version of modified MAE and MSE for ordinal classification tasks is expressed as below (Cardoso and Sousa, 2011).</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     MAE = (1/<i>N</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <i>c</i><sub style="font-size: 0.7em;">ij</sub> |<i>i</i>&#8722;<i>j</i>|
    </span>
   </p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     MSE = (1/<i>N</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <i>c</i><sub style="font-size: 0.7em;">ij</sub> (<i>i</i>&#8722;<i>j</i>)&#178;
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where <i>c</i><sub style="font-size: 0.75em;">ij</sub> is the entry in the <i>i</i><sup style="font-size: 0.7em;">th</sup> row and the <i>j</i><sup style="font-size: 0.7em;">th</sup> column in confusion matrix, <i>N</i> is total number of cases in the testing data (i.e., the sum of all entries in confusion matrix).</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Cardoso, J. S., &amp; Sousa, R. (2011). Measuring the performance of ordinal classification. International Journal of Pattern Recognition and Artificial Intelligence, 25(08), 1173-1195.</li>
    <li>Amig&#243;, E., Gonzalo, J., Mizzaro, S., &amp; Carrillo-de-Albornoz, J. (2020). An effectiveness metric for ordinal classification: Formal properties and experimental results. arXiv preprint arXiv:2006.01245.</li>
   </ul>
  </div>
"""

_KENDALL = """
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">An example metric for the third approach: Kendall's Tau-B</h3>
   <p style="color: #333; line-height: 1.6;">Named after Maurice Kendall, who developed it in 1938, Kendall's &#964; coefficient (also known as the Kendall rank correlation coefficient) is a non-parametric measure for degree of similarity between two sets of ranks given to a same set of cases. It respects the ranking of cases and does not require absolute values. There exist several versions of Kendall's Tau.</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Tau-A and Tau-B are used for square tables, where number of columns equals number of rows. Tau-B makes adjustments for ties, while Tau-A not.</li>
    <li>Tau-C is used for rectangular tables and essentially the same as Tau-B for square tables.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">In our case where the classifier attempts to classify the data into <i>k</i> desired categories and the reference standard also consists of <i>k</i> categories, Tau-B applies. Hence we only show Tau-B definition below and omit other variants here.</p>
   <p style="color: #333; line-height: 1.6;">Consider any two cases <i>i</i>, <i>j</i> in the testing data, denote their true labels as <i>y</i><sub style="font-size: 0.75em;">i</sub>, <i>y</i><sub style="font-size: 0.75em;">j</sub> and predicted labels as &#375;<sub style="font-size: 0.75em;">i</sub>, &#375;<sub style="font-size: 0.75em;">j</sub>. The pair of (<i>y</i><sub style="font-size: 0.75em;">i</sub>, <i>y</i><sub style="font-size: 0.75em;">j</sub>) and (&#375;<sub style="font-size: 0.75em;">i</sub>, &#375;<sub style="font-size: 0.75em;">j</sub>) is said to be <i>concordant</i> if the sort order for the pair agrees, i.e., either both <i>y</i><sub style="font-size: 0.75em;">i</sub> &gt; <i>y</i><sub style="font-size: 0.75em;">j</sub> and &#375;<sub style="font-size: 0.75em;">i</sub> &gt; &#375;<sub style="font-size: 0.75em;">j</sub> hold or both <i>y</i><sub style="font-size: 0.75em;">i</sub> &lt; <i>y</i><sub style="font-size: 0.75em;">j</sub> and &#375;<sub style="font-size: 0.75em;">i</sub> &lt; &#375;<sub style="font-size: 0.75em;">j</sub>), <i>discordant</i> if (<i>y</i><sub style="font-size: 0.75em;">i</sub> &gt; <i>y</i><sub style="font-size: 0.75em;">j</sub> and &#375;<sub style="font-size: 0.75em;">i</sub> &lt; &#375;<sub style="font-size: 0.75em;">j</sub>) or (<i>y</i><sub style="font-size: 0.75em;">i</sub> &lt; <i>y</i><sub style="font-size: 0.75em;">j</sub> and &#375;<sub style="font-size: 0.75em;">i</sub> &gt; &#375;<sub style="font-size: 0.75em;">j</sub>), and <i>tied</i> if <i>y</i><sub style="font-size: 0.75em;">i</sub> = <i>y</i><sub style="font-size: 0.75em;">j</sub> or &#375;<sub style="font-size: 0.75em;">i</sub> = &#375;<sub style="font-size: 0.75em;">j</sub>. &#964;<sub style="font-size: 0.75em;">B</sub> is defined as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     &#964;<sub style="font-size: 0.7em;">B</sub> = (<i>n</i><sub style="font-size: 0.7em;">c</sub> &#8722; <i>n</i><sub style="font-size: 0.7em;">d</sub>) / &#8730;[(<i>n</i><sub style="font-size: 0.7em;">0</sub> &#8722; <i>n</i><sub style="font-size: 0.7em;">1</sub>)(<i>n</i><sub style="font-size: 0.7em;">0</sub> &#8722; <i>n</i><sub style="font-size: 0.7em;">2</sub>)]
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li><i>n</i><sub style="font-size: 0.75em;">c</sub> = number of concordant pairs,</li>
    <li><i>n</i><sub style="font-size: 0.75em;">d</sub> = number of discordant pairs,</li>
    <li><i>n</i><sub style="font-size: 0.75em;">0</sub> = <i>N</i>(<i>N</i> - 1)/2 i.e., total number of pairs,</li>
    <li><i>n</i><sub style="font-size: 0.75em;">1</sub> = &#8721; <i>t</i><sub style="font-size: 0.75em;">l</sub>(<i>t</i><sub style="font-size: 0.75em;">l</sub> - 1)/2,</li>
    <li><i>n</i><sub style="font-size: 0.75em;">2</sub> = &#8721; <i>u</i><sub style="font-size: 0.75em;">m</sub>(<i>u</i><sub style="font-size: 0.75em;">m</sub> - 1)/2,</li>
    <li><i>t</i><sub style="font-size: 0.75em;">l</sub> = number of tied values in the <i>l</i><sup style="font-size: 0.7em;">th</sup> category for their predicted labels,</li>
    <li><i>u</i><sub style="font-size: 0.75em;">m</sub> = number of tied values in the <i>m</i><sup style="font-size: 0.7em;">th</sup> category for their true labels.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">The Kendall's Tau-B has a range of [&#8722;1, 1]. A value of 1 represents full agreement between the ranking order of two variables, and value of -1 represents a full disagreement. A higher value of the Kendall correlation indicates a higher ordinal association between the two variables.</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Some remarks about main advantages (or disadvantage) of using Kendall's tau:</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Reynolds (1977) concluded that among the many types of nonparametric methods in use, Kendall's tau is arguably the least problematic procedure conventionally used to evaluate associations among ordinal data.</li>
    <li>Newson (2002, p47) references Kendall &amp; Gibbons (1990) as arguing that "...confidence intervals for Spearman's <i>r</i><sub style="font-size: 0.75em;">S</sub> are less reliable and less interpretable than confidence intervals for Kendall's &#964;-parameters".</li>
    <li>Kendall's tau can be interpreted directly in terms of the probabilities of observing agreeable (concordant) and non-agreeable (discordant) pairs. This makes it easier to understand and explain the results.</li>
    <li>Kendall's tau should be used other than Spearman's Rho (introduced below) in small samples with many tied ranks (Field, 2009).</li>
    <li>If you consider one of your variables as an independent variable and the other as a dependent variable, you might consider running a Somers' d test instead. One may consider Somer's D as a modification of gamma designed to handle the case where one variable is dependent on another variable. Though Gamma and Somer's D are not presented here, one may refer to Agresti (2010) for details.</li>
   </ul>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Agresti, A. (2010). Analysis of ordinal categorical data (Vol. 656). John Wiley &amp; Sons.</li>
    <li>Field, A. (2009). Discovering statistics using SPSS (3rd Edition). London: Sage Publications.</li>
    <li>Kendall, M. G. (1938). A new measure of rank correlation. Biometrika, 30(1/2), 81-93.</li>
    <li>Kendall, M. G., &amp; Gibbons, J. D. (1990). Rank Correlation Methods. 5th ed. London: Griffin.</li>
    <li>Newson R. (2002). Parameters behind "nonparametric" statistics: Kendall's tau, Somers' D and median differences. Stata Journal 2002; 2(1):45-64.</li>
    <li>Reynolds HT (1977). The analysis of cross classifications. New York NY: Free Press.</li>
    <li>Sakai, T. (2020). Evaluating evaluation measures for ordinal classification and ordinal quantification. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 2759-2769).</li>
    <li>Smith, W. D., Dutton, R. C., &amp; Smith, N. T. (1996). A measure of association for assessing prediction accuracy that is a generalization of non&#8208;parametric ROC area. Statistics in Medicine, 15(11), 1199-1215.</li>
   </ul>
  </div>
"""

_PRED_PROB = """
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">An example metric for the third approach: prediction probability</h3>
   <p style="color: #333; line-height: 1.6;">Smith et al. (1996) proposed a metric, referred to as <i>prediction probability</i>, also called <i>prediction probability score</i>, or <i>prediction probability concordance</i> elsewhere (e.g., Petrick et al., 2021), denoted as <i>P</i><sub style="font-size: 0.75em;">k</sub>, to measure association between two variables.</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     <i>P</i><sub style="font-size: 0.7em;">k</sub> = (<i>n</i><sub style="font-size: 0.7em;">c</sub> + 0.5 <i>n</i><sub style="font-size: 0.7em;">1</sub>) / (<i>n</i><sub style="font-size: 0.7em;">c</sub> + <i>n</i><sub style="font-size: 0.7em;">d</sub> + <i>n</i><sub style="font-size: 0.7em;">1</sub>)
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where <i>n</i><sub style="font-size: 0.75em;">c</sub>, <i>n</i><sub style="font-size: 0.75em;">d</sub>, <i>n</i><sub style="font-size: 0.75em;">1</sub> were discussed in the Kendall's Tau-B section. In the case of comparing AI algorithm to a non-reference standard, <i>n</i><sub style="font-size: 0.75em;">1</sub> is the number of ties in the AI algorithm results (Petrick et al., 2021).</p>
   <p style="color: #333; line-height: 1.6;">From the defining formula, we can see this measure can be considered as the probability that the AI classifier ranks two randomly chosen cases in the same order as the reference classifier. It is also an extension of the trapezoidal area under the receiver operating characteristics curve (AUC) calculation (Petrick et al., 2021) to more than 2, ordinal classes in truth.</p>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Petrick, N., Akbar, S., Cha, K. H., Nofech-Mozes, S., Sahiner, B., Gavrielides, M. A., ... &amp; Martel, A. L. (2021). SPIE-AAPM-NCI BreastPathQ Challenge: an image analysis challenge for quantitative tumor cellularity assessment in breast cancer histology images following neoadjuvant treatment. Journal of Medical Imaging, 8(3), 034501.</li>
    <li>Smith, W. D., Dutton, R. C., &amp; Smith, N. T. (1996). A measure of association for assessing prediction accuracy that is a generalization of non&#8208;parametric ROC area. Statistics in Medicine, 15(11), 1199-1215.</li>
   </ul>
  </div>
"""

_SPEARMAN = """
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">An example metric for the third approach: Spearman's Rho</h3>
   <p style="color: #333; line-height: 1.6;">Spearman's Rho, also referred to as Spearman's rank correlation, usually denoted by &#961;, is a non-parametric measure that evaluates the rank correlation or statistical dependence between two variables. It quantifies the extent to which the relationship between the variables can be described by a monotonic function.</p>
   <p style="color: #333; line-height: 1.6;">Spearman's Rho is defined as Pearson correlation coefficient between the rank variables (Myers et al., 2010). Consider testing data with ground truth <i>Y</i> and the classifier to be evaluated &#375;, converting the true labels to ranks <i>R</i>(<i>Y</i>) and predicted labels to <i>R</i>(&#375;), then Spearman's Rho is computed as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     &#961; = cov(<i>R</i>(<i>Y</i>), <i>R</i>(&#375;)) / [&#963;<sub style="font-size: 0.7em;">R(Y)</sub> &#963;<sub style="font-size: 0.7em;">R(&#375;)</sub>]
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>cov(<i>R</i>(<i>Y</i>), <i>R</i>(&#375;)) is the covariance of the rank variables,</li>
    <li>&#963;<sub style="font-size: 0.75em;">R(Y)</sub> and &#963;<sub style="font-size: 0.75em;">R(&#375;)</sub> are standard deviations of rank variables.</li>
   </ul>
  </div>
  <div style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Myers, J. L., Well, A., &amp; Lorch, R. F. (2010). Research design and statistical analysis. Routledge.</li>
   </ul>
  </div>
"""

NODE = {
    "id": "N1_5",
    "title": "Multi-Class Classification: Metrics based on level of measurement",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "Weighted Cohen's Kappa": {
            "html": _WEIGHTED_KAPPA, "latex": []},
        "Mean Absolute Error (MAE) or Mean Square Error (MSE)": {
            "html": _MAE_MSE, "latex": []},
        "Kendall's Tau-B": {
            "html": _KENDALL, "latex": []},
        "Prediction probability": {
            "html": _PRED_PROB, "latex": []},
        "Spearman's Rho": {
            "html": _SPEARMAN, "latex": []},
    },
}

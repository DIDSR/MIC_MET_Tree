# tree/nodes/n03_binary_curve.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_roc   = get_image_base64(f"{IMG_BASE_PATH}G03binaryROCoverview_Fig1_300.jpg")
_img_auroc = get_image_base64(f"{IMG_BASE_PATH}G03binaryAUROC_Fig1C.jpg")
_img_pauc  = get_image_base64(f"{IMG_BASE_PATH}G03binaryPartialAUROC_Fig1C.jpg")
_img_pr    = get_image_base64(f"{IMG_BASE_PATH}G03binaryPRcurve_FigC.jpg")
_img_proc0 = get_image_base64(f"{IMG_BASE_PATH}G03binaryareaunderPartialROC_Fig0C.jpg")
_img_proc1 = get_image_base64(f"{IMG_BASE_PATH}G03binaryareaunderPartialROC_Fig1C.jpg")

def _img_tag(img_b64, alt):
    if img_b64:
        return (f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="data:image/jpeg;base64,{img_b64}" alt="{alt}" '
                f'style="max-width:100%;height:auto;border:1px solid #ddd;'
                f'border-radius:4px;padding:5px;"></div>')
    return '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_OVERVIEW = """
<div style="margin-bottom: 1.5rem;">
 <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
 <p style="color: #333; line-height: 1.6;">Now you have identified your task is a <i>binary</i> classification task based on a <i>reference standard with negligible variability</i> and <i>non-binary AI/ML output</i>. The evaluation metrics used for this type of classification problem are typically based on operating curves analysis such as ROC analysis, PR analysis. You may choose one option from the list at the bottom to learn more.</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #1a202c;">Metrics based on operating curve</h3>
 <p style="color: #666; margin-top: 1rem; font-style: italic;">(Please select a metric from the dropdown to view its details.)</p>
</div>
"""

_ROC_HTML = f"""
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">ROC analysis</h3>
 <p style="color: #333; line-height: 1.6;">For a classifier with a scalar output, one can obtain different (sensitivity, specificity) pairs by applying a decision threshold to the classifier output. The ROC curve shows the relationship between sensitivity (the true-positive fraction) and 1-specificity (the false-positive fraction) for every possible decision threshold (Metz, 1998; Obuchowski, 2003).</p>
 <p style="color: #333; line-height: 1.6;">Watch this video explanation of ROC, created by Brandon Gallas, PhD, US Food and Drug Administration, Center for Devices and Radiological Health. The link is <a href="https://vimeo.com/751670299" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://vimeo.com/751670299</a>.</p>
 {_img_tag(_img_roc, "Figure: ROC curve comparison showing Classifier A and Classifier B")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">Figure: ROC curve comparison between Classifier A and Classifier B</p>
 <p style="color: #333; line-height: 1.6;">The ROC curve and metrics derived from it measure the discrimination ability of the classifier between positive and negative classes. A classifier with no discrimination ability has a diagonal ROC curve in the (sensitivity,1-specificity) space. Classifier A in the figure above has an ROC curve above that of classifier B, and appears to provide better discrimination because at all specificities, it has a higher sensitivity than classifier B. Whether the difference in the discrimination ability between different classifiers measured by an ROC curve is significant can be investigated using an appropriate metric and an appropriate statistical test (Wagner et al., 2007). Select options at the bottom of this page to learn more.</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Metz, C. E. (1998). Basic principles of ROC analysis. <i>Semin Nucl Med, 8</i>(4), 283-98.</li>
   <li>Obuchowski, N. A. (2003). Receiver operating characteristic curves and their use in radiology. <i>Radiology, 229</i>(1), 3-8.</li>
   <li>Wagner, R. F., Metz, C. E., &amp; Campbell, G. (2007). Assessment of medical imaging systems and computer aids: A tutorial review. <i>Acad Radiol, 14</i>(6), 723-48.</li>
 </ul>
</div>
"""

_AUROC_HTML = f"""
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Area under the ROC curve and analysis of the entire curve</h3>
 <p style="color: #333; line-height: 1.6;">The area under the ROC curve, often abbreviated as AUROC or AUC, is a commonly used metric to measure the ability of the classifier output to separate positive and negative cases (Figure 1).</p>
 {_img_tag(_img_auroc, "Figure 1: AUROC measures the separability between the positive and negative classes at the classifier output")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">Figure 1: AUROC measures the separability between the positive and negative classes at the classifier output. The left column shows classifier output histograms for 400 negative and 400 positive cases, with different separations between the positive and negative classes at each row. The right column shows the ROC curves, the AUROC, and the 95% confidence intervals of AUROC at each row.</p>
 <p style="color: #333; line-height: 1.6;">By definition, AUROC represents the average sensitivity over all values of specificities. It can also be shown to be equal to the probability that when the classifier output for a positive case is a randomly paired with the classifier output for a negative case, the classifier output for the positive case is larger (Hanley and McNeil, 1982). AUROC can be estimated using semi-parametric methods, with the assumption that a monotonic transformation of the classifier output follows a given distribution (Metz and Pan, 1999), or using non-parametric methods that do not use any distributional assumptions (DeLong et al., 1988).</p>
 <p style="color: #333; line-height: 1.6;">To compare model performance on the same sample, two ROC curves are (partially) "paired" (or sometimes termed "correlated" in the literature) (DeLong et al., 1988; Hanley and McNeil, 1983). This comparison can be based on AUROC, ROC shape, a given specificity or confidence bands.</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Resources and notes for computing AUROC and its confidence intervals.</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>The R package "pROC" provides tools to visualize the ROC curve, estimate AUROC using both non-parametric and parametric approaches, and estimate confidence intervals. It also provides bootstrap methods to compare the area under curve for multiple ROC curves.</li>
   <li>The iMRMC package, in addition to providing estimates to AUROC and its confidence intervals, helps analyze the data when there are multiple models (computer classifiers or human readers) that provide scores for the cases (multi-reader multi-case, or MRMC analysis), and comparing classifiers when a study is not fully-paired e.g., (different classifiers provide scores for partially-overlapping sets of cases) (Gallas, 2006).</li>
   <li>The Metz ROC Software provides a nearly platform-independent software package for ROC analysis that includes many alternative ROC analysis approaches.</li>
   <li>The OR-DBM MRMC 3.0 package provides methods for analyzing AUROC for multi-reader multi-case (MRMC) ROC studies.</li>
 </ul>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Hanley, J. A., &amp; McNeil, B. J. (1982). The meaning and use of the area under a receiver operating characteristic (ROC) curve. <i>Radiology, 143</i>(1), 29-36.</li>
   <li>Metz, C. E., &amp; Pan, X. (1999). "Proper" Binormal ROC Curves: Theory and Maximum-Likelihood Estimation. <i>J Math Psychol, 43</i>(1), 1-33.</li>
   <li>DeLong, E. R., DeLong, D. M., &amp; Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. <i>Biometrics, 44</i>(3), 837-45.</li>
   <li>Gallas, B. D. (2006). One-shot estimate of MRMC variance: AUC. <i>Acad Radiol, 13</i>(3), 353-62.</li>
   <li>Hanley, J. A., &amp; McNeil, B. J. (1983). A method of comparing the areas under receiver operating characteristic curves derived from the same cases. <i>Radiology, 148</i>, 839-843.</li>
 </ul>
</div>
"""

_PAUC_HTML = f"""
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Partial area under the ROC curve</h3>
 <p style="color: #333; line-height: 1.6;">Rather than use the area under the entire ROC curve (AUC) this metric, the partial area under the ROC curve or pAUC, summarizes an ROC curve specifically in a clinically relevant region, typically a high-sensitivity region or high-specificity region. The partial area index can be interpreted as the average value of specificity over all values of sensitivity (Figure 1) or the average value of sensitivity over a range of values of specificity.</p>
 {_img_tag(_img_pauc, "Figure 1: Partial area under the ROC curve")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">Figure 1: Partial area under the ROC curve illustration</p>
 <p style="color: #333; line-height: 1.6;">To compare model performance on the same sample, two ROC curves are (partially) "paired" (or sometimes termed "correlated" in the literature) (Robin et al., 2011; Hanley and McNeil, 1983). This comparison can be based on AUC, ROC shape, a given specificity or confidence bands. Partial area under the ROC curves are often used to evaluate models within a range of high sensitivity or specificity. Several tests are implemented in pROC (Robin et al., 2011), including a bootstrap test to compare AUC or pAUC.</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Resources and notes for computing the partial area under the ROC curve.</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Jiang et al. (1996) developed a semi-parametric method to estimate the pAUC and its variance.</li>
 </ul>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>McClish, D. K. (1989). Analyzing a portion of the ROC curve. <i>Med Decis Making, 9</i>(3), 190-5.</li>
   <li>Jiang, Y., Metz, C. E., &amp; Nishikawa, R. M. (1996). A receiver operating characteristic partial area index for highly sensitive diagnostic tests. <i>Radiology, 201</i>(3), 745-50.</li>
   <li>Robin, X., Turck, N., Hainard, A., Tiberti, N., Lisacek, F., Sanchez, J. C., &amp; M&#252;ller, M. (2011). pROC: an open-source package for R and S+ to analyze and compare ROC curves. <i>BMC Bioinformatics, 12</i>, 77.</li>
   <li>Hanley, J. A., &amp; McNeil, B. J. (1983). A method of comparing the areas under receiver operating characteristic curves derived from the same cases. <i>Radiology, 148</i>, 839-843.</li>
   <li>DeLong, E. R., DeLong, D. M., &amp; Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. <i>Biometrics, 44</i>(3), 837-45.</li>
 </ul>
</div>
"""

_PR_HTML = f"""
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Area under the precision-recall curve</h3>
 {_img_tag(_img_pr, "Figure: Precision-Recall curve")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">Figure: Precision-Recall curve illustration</p>
 <p style="color: #333; line-height: 1.6;">A <b>precision-recall curve</b> (PRC) is a graph showing the relationship between precision (= positive predictive value) and recall (= sensitivity) for every possible cut-off, with:</p>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>the x-axis showing recall = sensitivity = TP / (TP + FN)</li>
   <li>the y-axis showing precision = positive predictive value = TP / (TP + FP)</li>
 </ul>
 <p style="color: #333; line-height: 1.6;">and may be used as a supplement to the routinely used ROC curves, especially in the case of imbalanced datasets.</p>
 <p style="color: #333; line-height: 1.6;">Note that precision (equivalent to PPV) is not intrinsic to the AI/ML system, i.e., for the same AI/ML system, the use of a test data set with a different prevalence of disease will change the PPV. The curve for a 'baseline' (random guessing) classifier (see Figure above) similarly depends on the prevalence in your dataset. Therefore, when making statistical inference based on a finite sample, it is important to match the disease prevalence in the sample to that in the true population (or to employ a carefully designed correction method to consider the difference in prevalences) (Sahiner et al., 2017).</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Resources and notes that may be useful for estimating the area under precision-recall curve.</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Boyd et al. (2013) provide several approaches to compute the point estimate and confidence interval for the area under the precision-recall curve.</li>
   <li>R package "precrec" (Saito and Rehmsmeier, 2017) can be used to compute the point estimate and confidence intervals for the area under PRC and plot the curve.</li>
   <li>R code for the article above (Boyd et al., 2013) is also provided by the author in GitHub: <a href="https://github.com/kboyd/raucpr" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://github.com/kboyd/raucpr</a>.</li>
   <li>As noted above, precision is not intrinsic to the AI/ML system and depends on disease prevalence. Zhou et al. (2009) and Mercaldo et al. (2007) provide methods for calculating point estimates and the corresponding confidence intervals for the condition when the data set does not reflect the true disease prevalence, but the true prevalence is known.</li>
 </ul>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Other packages that can be used to compute the area under PRC and/or plot the curve include:</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>R package "ROCR" to compute the area under PRC and to plot the curve ("performance" function).</li>
   <li>R package "PRROC" to compute the area under PRC (pr.curve function) and to plot the curve.</li>
   <li>R package "MLmetrics" to compute the area under PRC ("PRAUC" function).</li>
 </ul>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Sahiner, B., Chen, W., Pezeshk, A., &amp; Petrick, N. (2017, March). Comparison of two classifiers when the data sets are imbalanced: the power of the area under the precision-recall curve as the figure of merit vs. the area under the ROC curve. In <i>Medical Imaging 2017: Image Perception, Observer Performance, and Technology Assessment</i> (Vol. 10136, p. 101360G). International Society for Optics and Photonics.</li>
   <li>Boyd, K., Eng, K. H., &amp; Page, C. D. (2013). Area under the precision-recall curve: point estimates and confidence intervals. In <i>Joint European conference on machine learning and knowledge discovery in databases</i> (pp. 451-466). Springer, Berlin, Heidelberg.</li>
   <li>Saito, T., &amp; Rehmsmeier, M. (2017). Precrec: fast and accurate precision-recall and ROC curve calculations in R. <i>Bioinformatics, 33</i>(1), 145-147.</li>
   <li>Zhou, X. H., McClish, D. K., &amp; Obuchowski, N. A. (2009). <i>Statistical methods in diagnostic medicine</i> (Vol. 569). John Wiley &amp; Sons.</li>
   <li>Mercaldo, N. D., Lau, K. F., &amp; Zhou, X. H. (2007). Confidence intervals for predictive values with an emphasis to case-control studies. <i>Stat Med, 26</i>(10), 2170-2183.</li>
 </ul>
</div>
"""

_PROC_HTML = f"""
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Area (and partial area) under the PROC curve</h3>
 {_img_tag(_img_proc0, "Figure: PROC curve overview")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; font-size: 0.9rem;">Figure: Predictive receiver operating characteristic (PROC) curve</p>
 <p style="color: #333; line-height: 1.6;">The predictive receiver operating characteristic (PROC) is used in the evaluation of probabilistic two class predictions, where the vertical axis indicates the positive predicted value (PPV) and the horizontal axis indicates the negative predicted value (NPV). The PROC curve differs from the more well-known receiver operating characteristic (ROC) curve as it takes into account disease prevalence (Hughes, 2020). PROC provides a basis for evaluation using metrics defined conditionally on the outcome of the prediction (e.g. prediction from ML and AI model) rather than metrics defined conditionally on the actual disease status.</p>
 <p style="color: #333; line-height: 1.6;">The shape of PROC curve can be characterized by the difference between the means of two classes, the ratio of the standard deviations of two classes, and prevalence. Figure 1 depicts the examples of PROC by the ratio of two standard deviations from two classes being less than 1, equal to 1 and greater than 1 for a fixed mean of difference in two classes, and two high and low prevalence rates (modified from Shiu and Gatsonis, 2008).</p>
 <p style="color: #333; line-height: 1.6;">Area under curves can be used to summarize the predictive performance of a diagnostic test when a PROC curve or a segment of interest is monotone, not in a full range of 0 to 100% (Hughes, 2020; Shiu and Gatsonis, 2008). The (partial) area also can be used and interpreted as the average positive predictive value corresponding to a given range of negative predictive value or vice versa. Comparisons of area under the curves can be made by the delta method (Shiu and Gatsonis, 2008).</p>
 <p style="color: #333; line-height: 1.6;">The details of optimal method of choosing the maximum point of PSEP (PPV &#8722; (1-NPV) = PPV+NPV-1) or r = 1-PSEP can be found (Shiu and Gatsonis, 2008; Hughes et al., 2020).</p>
 <p style="color: #333; line-height: 1.6;">When the variability of disease is smaller than its no-disease group (Figure 1.a), PPV value starts from the vertical axis (i.e. 1- NPV=0), crossing the main diagonal from above (PPV=1- NPV=prevalence), and continue the horizontal axis (where PPV=0). When the variability of disease is same as its no-disease group (Figure 1.b), PPV value starts from the vertical axis (i.e. 1- NPV=0), and continues the upper horizontal of axis (where PPV=1) without crossing the main diagonal. When the variability of disease is larger than its no-disease group (Figure 1.c), PPV value starts from the horizontal axis (i.e. PPV=1), crossing the main diagonal from above (PPV=1- NPV=prevalence), and continue the vertical axis (where 1 - NPV=1)</p>
 {_img_tag(_img_proc1, "Figure 1: Predictive curves with different parameters")}
 <p style="color: #666; margin-top: 0.5rem; font-style: italic; text-align: center; font-size: 0.9rem;">Figure 1. Predictive curves a=0.8. (a) b=0.7, (b) b=1, (c) b=1.5. The value of "a" is the difference between the two means of classes and the value of "b" is the ratio of two standard deviations from two classes (i.e. ratio= SD(disease)/SD (no disease). p=prevalence. Solid line, high prevalence (p=0.7); dot-dashed line, low prevalence (p=0.3). (figure from Shiu, 2008, used with permission from The Royal Society.)</p>
 <p style="color: #333; line-height: 1.6;">The area (A1) under a monotone segment of the PROC curve can be interpreted as the average positive predictive value over a range of NPV. Similarly, the area (A2) under a monotone segment of the PROC curve can be interpreted as the average negative predictive value over a range of PPV. Comparable areas can suggest that a model simultaneously reach a satisfactory level.</p>
</div>
<div style="margin-bottom: 1.5rem;">
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
 <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
   <li>Hughes, G. (2020). On the Binormal Predictive Receiver Operating Characteristic Curve for the Joint Assessment of Positive and Negative Predictive Values. <i>Entropy, 22</i>(6), 593.</li>
   <li>Shiu, S. Y., &amp; Gatsonis, C. (2008). The predictive receiver operating characteristic curve for the joint assessment of the positive and negative predictive values. <i>Philos Trans A Math Phys Eng Sci, 366</i>(1874), 2313-33.</li>
   <li>Hughes, G., Kopetzky, J., &amp; McRoberts, N. (2020). Mutual Information as Performance Measure for Binary Predictors Characterized by Both ROC Curve and PROC Curve Analysis. <i>Entropy, 22</i>(9), 938.</li>
 </ul>
</div>
"""

NODE = {
    "id": "N0_3",
    "title": "Binary classification \u2013 metrics based on operating curves",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "ROC analysis": {
            "html": _ROC_HTML,
            "latex": [],
            "sub_metrics": {
                "Area under ROC curve": {
                    "html": _AUROC_HTML,
                    "latex": [],
                },
                "Partial area under ROC curve": {
                    "html": _PAUC_HTML,
                    "latex": [],
                },
            },
        },
        "Area under PR curve": {
            "html": _PR_HTML,
            "latex": [],
        },
        "Area (and partial area) under Predictive operating characteristic (PROC) curve": {
            "html": _PROC_HTML,
            "latex": [],
        },
    },
}

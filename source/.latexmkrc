# Run latexmk from the repository root so project-relative paths resolve.
@default_files = ('source/thesis.tex');
$do_cd = 0;
$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';

# Keep intermediate files separate from the PDF and SyncTeX output.
$aux_dir = '.output/.build';
$out_dir = '.output';

# Expose the most recent log alongside the PDF, including on build failure.
$success_cmd = $failure_cmd = 'internal publish_build_log %Y %Z %R';
sub publish_build_log {
    my ($aux, $output, $job) = @_;
    my $log = "$aux$job.log";
    return 0 if $aux eq $output || !-f $log;
    File::Copy::copy($log, "$output$job.log") or die "Could not copy $log: $!\n";
    return 0;
}

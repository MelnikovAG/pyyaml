
import test_appliance

from yaml.scanner import *

class TestTokens(test_appliance.TestAppliance):

    # Tokens mnemonic:
    # directive:            %
    # document_start:       ---
    # document_end:         ...
    # alias:                *
    # anchor:               &
    # tag:                  !
    # scalar                _
    # block_sequence_start: [[
    # block_mapping_start:  {{
    # block_end:            ]}
    # flow_sequence_start:  [
    # flow_sequence_end:    ]
    # flow_mapping_start:   {
    # flow_mapping_end:     }
    # entry:                ,
    # key:                  ?
    # value:                :

    replaces = {
        YAMLDirectiveToken: '%',
        TagDirectiveToken: '%',
        ReservedDirectiveToken: '%',
        DocumentStartToken: '---',
        DocumentEndToken: '...',
        AliasToken: '*',
        AnchorToken: '&',
        TagToken: '!',
        ScalarToken: '_',
        BlockSequenceStartToken: '[[',
        BlockMappingStartToken: '{{',
        BlockEndToken: ']}',
        FlowSequenceStartToken: '[',
        FlowSequenceEndToken: ']',
        FlowMappingStartToken: '{',
        FlowMappingEndToken: '}',
        EntryToken: ',',
        KeyToken: '?',
        ValueToken: ':',
    }

    def _testTokens(self, test_name, data_filename, tokens_filename):
        tokens1 = None
        tokens2 = file(tokens_filename, 'rb').read().split()
        try:
            scanner = Scanner(data_filename, file(data_filename, 'rb').read())
            tokens1 = []
            while not isinstance(scanner.peek_token(), EndToken):
                tokens1.append(scanner.get_token())
            tokens1 = [self.replaces[t.__class__] for t in tokens1]
            self.failUnlessEqual(tokens1, tokens2)
        except:
            print
            print "DATA:"
            print file(data_filename, 'rb').read()
            print "TOKENS1:", tokens1
            print "TOKENS2:", tokens2
            raise

TestTokens.add_tests('testTokens', '.data', '.tokens')

class TestScanner(test_appliance.TestAppliance):

    def _testScanner(self, test_name, data_filename, canonical_filename):
        for filename in [canonical_filename, data_filename]:
            tokens = None
            try:
                scanner = Scanner(filename, file(filename, 'rb').read())
                tokens = []
                while not isinstance(scanner.peek_token(), EndToken):
                    tokens.append(scanner.get_token().__class__.__name__)
            except:
                print
                print "DATA:"
                print file(data_filename, 'rb').read()
                print "TOKENS:", tokens
                raise

TestScanner.add_tests('testScanner', '.data', '.canonical')
